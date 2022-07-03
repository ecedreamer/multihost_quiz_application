from django.contrib import admin
from .models import QuizSession, QuizStep, Question, Option

admin.site.register([QuizSession, QuizStep ])


class OptionInline(admin.TabularInline):
    model = Option


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [OptionInline]

admin.site.register(Question, QuestionAdmin)