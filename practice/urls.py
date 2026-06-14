from django.urls import path
from .views import HomeView, LessonDetailView, LessonListView, ResetProgressView

app_name = "practice"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("lessons/", LessonListView.as_view(), name="lesson_list"),
    path("lessons/<slug:slug>/", LessonDetailView.as_view(), name="lesson_detail"),
    path("reset/", ResetProgressView.as_view(), name="reset_progress"),
]
