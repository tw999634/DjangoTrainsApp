from django.db import models
from django.urls import reverse


class PracticeContent(models.Model):
    class Meta:
        db_table = 'content'

    slug = models.SlugField("URLスラッグ", unique=True)
    order = models.IntegerField("表示順", default=1)
    title = models.CharField("タイトル", max_length=120)
    concept = models.CharField("学習キーワード", max_length=80)
    summary = models.TextField("概要")
    explanation = models.TextField("詳細")
    practice_task = models.TextField("練習内容")
    starter_code = models.TextField("初期コード", blank=True)
    sample_solution = models.TextField("正解コード")
    required_patterns = models.TextField("正解判定用パターン")

    def get_absolute_url(self):
        return reverse("practice:lesson_detail", kwargs={"slug": self.slug})


class PracticeProgress(models.Model):
    class Meta:
        db_table = 'progress'

    content = models.OneToOneField(
        PracticeContent,
        verbose_name="練習コンテンツ",
        on_delete=models.CASCADE,
        related_name="progress",
    )
    is_completed = models.BooleanField("完了", default=False)
    last_submitted_code = models.TextField("最後に提出したコード", blank=True)


class PracticeSubmission(models.Model):
    class Meta:
        db_table = 'submission'

    content = models.ForeignKey(
        PracticeContent,
        verbose_name="練習コンテンツ",
        on_delete=models.CASCADE,
        related_name="submissions",
    )
    submitted_code = models.TextField("提出コード")
    is_correct = models.BooleanField("正解", default=False)

