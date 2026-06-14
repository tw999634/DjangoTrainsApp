import re

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from .forms import CodePracticeForm
from .models import PracticeContent, PracticeProgress, PracticeSubmission


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        lessons = list(PracticeContent.objects.all().order_by("order", "id"))
        completed_ids = set(
            PracticeProgress.objects.filter(
                content__in=lessons,
                is_completed=True,
            ).values_list("content_id", flat=True)
        )

        context["total_count"] = len(lessons)
        context["completed_count"] = len(completed_ids)
        context["remaining_count"] = len(lessons) - len(completed_ids)
        return context


class LessonListView(TemplateView):
    template_name = "lesson_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        lessons = list(PracticeContent.objects.all().order_by("order", "id"))
        completed_ids = set(
            PracticeProgress.objects.filter(
                content__in=lessons,
                is_completed=True,
            ).values_list("content_id", flat=True)
        )

        context["lessons"] = lessons
        context["completed_ids"] = completed_ids
        context["total_count"] = len(lessons)
        context["completed_count"] = len(completed_ids)
        return context


class ResetProgressView(View):
    def post(self, request):
        PracticeProgress.objects.update(
            is_completed=False,
            last_submitted_code="",
        )
        PracticeSubmission.objects.all().delete()
        messages.success(request, "学習進捗をリセットしました。")
        return redirect("practice:home")


class LessonDetailView(View):
    template_name = "lesson_detail.html"

    def build_context(self, content, progress, form=None, feedback=None, is_correct=None, pattern_errors=None):
        initial_code = progress.last_submitted_code or content.starter_code

        if form is None:
            form = CodePracticeForm(initial={"code": initial_code})

        return {
            "lesson": content,
            "progress": progress,
            "form": form,
            "is_completed": progress.is_completed,
            "feedback": feedback,
            "is_correct": is_correct,
            "expected_code": content.sample_solution,
            "pattern_errors": pattern_errors or [],
        }

    def judge_code(self, content, submitted_code):
        patterns = []
        for line in content.required_patterns.splitlines():
            pattern = line.strip()
            if pattern:
                patterns.append(pattern)

        if not patterns:
            return False, ["このレッスンには正解判定用パターンが登録されていません。"]

        missing_patterns = []
        for pattern in patterns:
            if not re.search(pattern, submitted_code, flags=re.MULTILINE | re.DOTALL):
                missing_patterns.append(pattern)

        return len(missing_patterns) == 0, missing_patterns


    def get(self, request, slug):
        content = PracticeContent.objects.get(slug=slug)
        progress, _ = PracticeProgress.objects.get_or_create(content=content)
        return render(request, self.template_name, self.build_context(content, progress))

    def post(self, request, slug):
        content = PracticeContent.objects.get(slug=slug)
        progress, _ = PracticeProgress.objects.get_or_create(content=content)

        form = CodePracticeForm(request.POST)
        feedback = None
        is_correct = False
        pattern_errors = []

        if form.is_valid():
            submitted_code = form.cleaned_data["code"]
            is_correct, pattern_errors = self.judge_code(content, submitted_code)

            if is_correct:
                feedback = "正解です。必要なコード要素が確認できたため、レッスンを完了しました。"
                progress.is_completed = True
            else:
                feedback = "正解ではありません。問題文と練習内容を確認して、もう一度書いてみましょう。"

            PracticeSubmission.objects.create(
                content=content,
                submitted_code=submitted_code,
                is_correct=is_correct,
                feedback=feedback,
            )

            progress.last_submitted_code = submitted_code
            progress.save()

        return render(
            request,
            self.template_name,
            self.build_context(
                content,
                progress,
                form=form,
                feedback=feedback,
                is_correct=is_correct,
                pattern_errors=pattern_errors,
            ),
        )
