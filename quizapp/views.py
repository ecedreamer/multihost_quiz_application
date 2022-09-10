import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from quizapp.models import Question, QuizSession, Submission
from authapp.utils import check_participant, check_host
from .forms import *


class ParticipantUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if check_participant(request.user):
            self.participant = check_participant(request.user)
        else:
            print("redirect to host participation create page so")

        return super().dispatch(request, *args, **kwargs)


class HostUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if check_host(request.user):
            self.host = check_host(request.user)
        else:
            print("redirect to host participation create page so")

        return super().dispatch(request, *args, **kwargs)


class QuizStartView(ParticipantUserMixin, View):
    template_name = "participants/quizstart.html"

    def get(self, request, uuid, *args, **kwargs):

        try:
            quiz = QuizSession.objects.get(unique_code=uuid)
            submission = Submission.objects.filter(quiz_session=quiz, participant_user=self.participant)
            if submission.exists() and not quiz.allow_multiple_submission:
                print("User has already submitted the answer so can not play now")
                return redirect("website:home")
            context = {
                "unique_code": uuid,
                "quiz": quiz,
                "questions": Question.objects.filter(quiz_session=quiz).order_by("position")
            }
        except Exception as e:
            print(e)
            return redirect("website:home")

        return render(request, self.template_name, context)

    def post(self, request, uuid, *args, **kwargs):
        try:
            quiz = QuizSession.objects.get(unique_code=uuid)
            answers = request.POST.get("answers_field")
            answers_json = json.loads(answers)
            result = self.check_answer(answers_json)
            return JsonResponse({"result": result})
        except Exception as e:
            print(f"Error occured: {e}")
        return redirect("quizapp:quizstart", uuid)

    def check_answer(self, client_answers: dict):
        if not isinstance(client_answers, dict):
            raise ValueError("Invalid data type, client_answers must be a dict object")
        result = {
            "right_answers": [],
            "wrong_answers": [],
            "obtained_scores": 0
        }
        for question, selected_options in client_answers.items():
            question_id = question.split("_")[1]
            question = Question.objects.get(id=question_id)
            right_options = question.option_set.filter(is_right_answer=True)
            if right_options.count() == 1:
                if right_options.first().position == selected_options:
                    result["right_answers"].append(question_id)
                    result["obtained_scores"] += 1
                else:
                    result["wrong_answers"].append(question_id)
            elif right_options.count() > 1:
                right_options_positions = [option.position for option in right_options]
                for option in selected_options:
                    if option in right_options_positions:
                        right_options_positions.remove(option)
                if not right_options_positions:
                    result["right_answers"].append(question_id)
                    result["obtained_scores"] += 1
                else:
                    result["wrong_answers"].append(question_id)
        return result



# host user

class HostDashboardView(HostUserMixin, View):
    template_name = "hosts/quizhostdashboard.html"
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)


class HostQuizSessionListView(HostUserMixin, View):
    template_name = "hosts/hostquizsessionlist.html"

    def get(self, request, *args, **kwargs):
        context = {
            "quiz_list": QuizSession.objects.filter(host_user=self.host)
        }
        return render(request, self.template_name, context)


class HostQuizSessionCreateView(HostUserMixin, View):
    template_name = "hosts/hostquizsessioncreate.html"

    def get(self, request, *args, **kwargs):
        context = {
            'form': QuizSessionForm
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        quiz_form = QuizSessionForm(data=request.POST)
        context = {
            'form': QuizSessionForm
        }
        if quiz_form.is_valid():
            quiz_form.instance.host_user = self.host
            quiz_session = quiz_form.save()
            return redirect("quizapp:hostquizsessionlist")
        else:
            print(quiz_form.errors)
            context['error'] = quiz_form.errors
            return render(request, self.template_name, context)


class HostQuizSessionDetailView(HostUserMixin, View):
    template_name = "hosts/hostquizsessiondetail.html"

    def get(self, request, unique_code, *args, **kwargs):
        quiz_session = QuizSession.objects.get(unique_code=unique_code)
        context = {
            'quiz_session': quiz_session,
            "question_list": quiz_session.question_set.order_by("position")
        }
        return render(request, self.template_name, context)
        

class HostQuizSessionAddQuestionView(HostUserMixin, View):
    def post(self, request, unique_code, *args, **kwargs):

        return redirect("quizapp:hostquizsessiondetail", unique_code)