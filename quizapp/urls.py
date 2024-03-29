from django.urls import path
from .views import *


app_name = "quizapp"

urlpatterns = [
    # as a player
    path("play-quiz/<uuid>/", QuizStartView.as_view(), name="quizstart"),

    # as a host
    path("hosts/", HostDashboardView.as_view(), name="quizhostdashboard"),
    path("hosts/quiz-list/", HostQuizSessionListView.as_view(), name="hostquizsessionlist"),
    path("hosts/quiz-create/", HostQuizSessionCreateView.as_view(), name="hostquizsessioncreate"),
    path("hosts/quiz-<unique_code>/", HostQuizSessionDetailView.as_view(), name="hostquizsessiondetail"),
    path("hosts/quiz-<unique_code>/add-question/", HostQuizSessionAddQuestionView.as_view(), name="hostquizsessionaddquestion"),
]