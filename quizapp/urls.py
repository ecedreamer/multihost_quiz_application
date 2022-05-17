from django.urls import path
from .views import QuizDetailView


app_name = "quizapp"

urlpatterns = [
    path("play-quiz/<uuid>/", QuizDetailView.as_view(), name="quizdetail"),
]