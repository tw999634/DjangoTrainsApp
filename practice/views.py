import re

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from .forms import CodePracticeForm
from .models import PracticeContent, PracticeProgress, PracticeSubmission


# トップページ
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 全体レッスンデータを読み込む
        lessons = list(PracticeContent.objects.all().order_by("order", "id"))
        completed_ids = list(
            PracticeProgress.objects.filter(
                is_completed=True,
            ).values_list("content_id", flat=True)
        )

        # 全体レッスン数、完了数、未完了数を計算
        context["total_count"] = len(lessons)
        context["completed_count"] = len(completed_ids)
        context["remaining_count"] = len(lessons) - len(completed_ids)
        return context


# 練習一覧ページ
class LessonListView(TemplateView):
    template_name = "lesson_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 全体レッスンデータを読み込む
        lessons = list(PracticeContent.objects.all().order_by("order", "id"))
        completed_ids = list(
            PracticeProgress.objects.filter(
                is_completed=True,
            ).values_list("content_id", flat=True)
        )

        # 全体レッスンの目録、完了レッスンの目録、全体レッスン数、完了数を渡す
        context["lessons"] = lessons
        context["completed_ids"] = completed_ids
        context["total_count"] = len(lessons)
        context["completed_count"] = len(completed_ids)
        return context


# 進捗リセット機能
class ResetProgressView(View):
    def post(self, request):

        # 全ての完了状態/最近提出コードデータを削除
        PracticeProgress.objects.update(
            is_completed=False,
            last_submitted_code="",
        )
        # コード提出記録を全て削除
        PracticeSubmission.objects.all().delete()
        
        # リセット完了メッセージを渡す
        messages.success(request, "学習進捗をリセットしました。")
        return redirect("practice:home")


# 学習ページ
class LessonDetailView(View):
    template_name = "lesson_detail.html"

    # context生成関数
    def build_context(self, content, progress, form=None, feedback=None, is_correct=None):
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
        }

    # 提出コードの採点結果判定関数
    def judge_code(self, content, submitted_code):
        patterns = []
        for line in content.required_patterns.splitlines():
            pattern = line.strip()
            if pattern:
                patterns.append(pattern)

        # 正規表現式と違うコードを検出
        missing_patterns = []
        for pattern in patterns:
            if not re.search(pattern, submitted_code, flags=re.MULTILINE | re.DOTALL):
                missing_patterns.append(pattern)

        # 採点結果を渡す
        return len(missing_patterns) == 0


    # 最初学習ページに入った場合
    def get(self, request, slug):
        content = PracticeContent.objects.get(slug=slug)
        progress, _ = PracticeProgress.objects.get_or_create(content=content)
        return render(request, self.template_name, self.build_context(content, progress))

    # コードを提出した場合
    def post(self, request, slug):
        content = PracticeContent.objects.get(slug=slug)
        progress, _ = PracticeProgress.objects.get_or_create(content=content)

        form = CodePracticeForm(request.POST)
        feedback = None
        is_correct = False

        if form.is_valid():
            submitted_code = form.cleaned_data["code"]
            is_correct = self.judge_code(content, submitted_code)

            # 採点結果
            if is_correct:
                feedback = "正解です。必要なコード要素が確認できたため、レッスンを完了しました。"
                progress.is_completed = True
            else:
                feedback = "正解ではありません。問題文と練習内容を確認して、もう一度書いてみましょう。"

            # 提出履歴を保存
            PracticeSubmission.objects.create(
                content=content,
                submitted_code=submitted_code,
                is_correct=is_correct,
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
            ),
        )
