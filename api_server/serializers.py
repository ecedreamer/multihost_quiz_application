from rest_framework import serializers
from django.contrib.auth import get_user_model
from quizapp.models import Option, QuizSession, Question


User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "date_joined", "is_active",
                  "full_name", "profile_image", "mobile_number"]


class QuestionPlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "position", "question", "has_multiple_answers"]


class QuizSessionPlaySerializer(serializers.ModelSerializer):
    question_set = QuestionPlaySerializer(many=True)

    class Meta:
        model = QuizSession
        fields = ["id", "title", "unique_code", "host_user", "total_questions",
                  "total_steps", "show_result_immediately", "is_time_bound", "time_in_minutes", "question_set"]





class OptionPlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["id", "position", "answer",]