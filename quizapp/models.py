from django.db import models
from authapp.models import TimeStamp, HostUser, ParticipantUser
import uuid 

class QuizSession(TimeStamp):
    title = models.CharField(max_length=200)
    unique_code = models.UUIDField(unique=True, default=uuid.uuid4)
    host_user = models.ForeignKey(HostUser, on_delete=models.CASCADE)
    total_questions = models.PositiveIntegerField()
    total_steps = models.PositiveIntegerField()
    show_result_immediately = models.BooleanField(default=True)
    is_time_bound = models.BooleanField(default=True)
    time_in_minutes = models.PositiveIntegerField(null=True, blank=True)
    start_together = models.BooleanField(default=False)
    submit_one_by_one = models.BooleanField(default=False)
    time_per_quiz_in_minutes = models.PositiveIntegerField(
        null=True, blank=True)
    allow_multiple_submission = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


# questions per steps
class QuizStep(TimeStamp):
    quiz_session = models.ForeignKey(QuizSession, on_delete=models.CASCADE)
    step_title = models.CharField(max_length=50)
    step_description = models.TextField(null=True, blank=True)


class Question(TimeStamp):
    quiz_session = models.ForeignKey(QuizSession, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    quiz_step = models.ForeignKey(
        QuizStep, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.CharField(max_length=1024)
    options_count = models.PositiveIntegerField(default=4)
    has_multiple_answers = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.question


class Option(TimeStamp):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    position = models.CharField(max_length=1)
    answer = models.CharField(max_length=500)
    is_right_answer = models.BooleanField(default=False)


class Submission(TimeStamp):
    participant_user = models.ForeignKey(
        ParticipantUser, on_delete=models.RESTRICT)
    quiz_session = models.ForeignKey(
        QuizSession, on_delete=models.RESTRICT, related_name="submissions")
    answers = models.TextField()
    time_taken_in_minutes = models.PositiveIntegerField()
    # answers = "{1:"a", 2: ["b", "d"], 3:"a"}"
