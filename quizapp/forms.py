from django import forms

from quizapp.models import QuizSession


class QuizSessionForm(forms.ModelForm):
    class Meta:
        model = QuizSession
        fields = ['title', 'total_questions', 'total_steps', 'show_result_immediately', 'is_time_bound',
                  'time_in_minutes', 'start_together', 'submit_one_by_one', 'time_per_quiz_in_minutes', 'allow_multiple_submission', 'is_public']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'total_questions': forms.NumberInput(attrs={"class": "form-control",}),
            'total_steps': forms.NumberInput(attrs={"class": "form-control",}),
            'show_result_immediately': forms.CheckboxInput(attrs={"class": "",}),
            'is_time_bound': forms.CheckboxInput(attrs={"class": "",}),
            'time_in_minutes': forms.NumberInput(attrs={"class": "form-control",}),
            'start_together': forms.CheckboxInput(attrs={"class": "",}),
            'submit_one_by_one': forms.CheckboxInput(attrs={"class": "",}),
            'time_per_quiz_in_minutes': forms.NumberInput(attrs={"class": "form-control",}),
            'allow_multiple_submission': forms.CheckboxInput(attrs={"class": "",}),
            'is_public': forms.CheckboxInput(attrs={"class": "",}),
        }
