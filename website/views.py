from django.shortcuts import render, redirect
from django.views.generic import View

from quizapp.models import QuizSession
from .forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from authapp.utils import check_host, check_participant


User = get_user_model()


class HomeView(View):
    template_name = "website/home.html"

    def get(self, request, *args, **kwargs):
        context = {
            "quizs": QuizSession.objects.all()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        try:
            uuid = request.POST.get("unique_code")
            QuizSession.objects.get(unique_code=uuid)
            return redirect("quizapp:quizdetail", uuid)
        except QuizSession.DoesNotExist as e:
            return redirect("website:home")

class LoginView(View):
    template_name = "website/login.html"

    def get(self, request, *args, **kwargs):
        context = {
            "login_form": LoginForm
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get("email")
            password = login_form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
            else:
                context = {
                    "login_form": LoginForm,
                    "error": "form is not valid"
                }
                return render(request, self.template_name, context)
        else:
            context = {
                "login_form": LoginForm,
                "error": "form is not valid"
            }
            return render(request, self.template_name, context)

        return redirect("website:home")


class RegisterView(View):
    template_name = "website/register.html"

    def get(self, request, *args, **kwargs):
        context = {
            "register_form": RegisterForm
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        register_form = LoginForm(data=request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get("email")
            password = register_form.cleaned_data.get("password")
            full_name = register_form.cleaned_data.get("full_name")
            user = User.objects.create_user(email, password, full_name)
            print(user)

        else:
            context = {
                "loginform": LoginForm,
                "error": "form is not valid"
            }
            return render(request, self.template_name, context)

        return redirect("website:home")



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("website:home")