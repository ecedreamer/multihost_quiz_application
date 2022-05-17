from django.shortcuts import render, redirect
from django.views.generic import View

from quizapp.models import Question, QuizSession
from authapp.utils import check_participant

class ParticipantUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if check_participant(request.user):
            self.participant = check_participant(request.user)
        else:
            print("hello")

        return super().dispatch(request, *args, **kwargs)


class QuizDetailView(ParticipantUserMixin, View):
    template_name = "participants/quizdetail.html"

    def get(self, request, uuid, *args, **kwargs):

        try:
            quiz = QuizSession.objects.get(unique_code=uuid)
            context = {
                "unique_code": uuid,
                "quiz": quiz,
                "questions": Question.objects.filter(quiz_session=quiz).order_by("position")
            }
        except Exception as e:
            return

        return render(request, self.template_name, context)

    def post(self, request, uuid, *args, **kwargs):
        try:
            quiz = QuizSession.objects.get(unique_code=uuid)
            print(request.POST)
        except Exception as e:
            return
        return redirect("quizapp:quizdetail", uuid)
