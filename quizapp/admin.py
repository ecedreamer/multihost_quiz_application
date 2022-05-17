from django.contrib import admin
from .models import QuizSession, QuizStep, Question, Option

admin.site.register([QuizSession, QuizStep, Question, Option, ])