from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    #quiz_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    about = models.TextField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    #question_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField()
    quiz = models.ManyToManyField(Quiz)

    def __str__(self):
        return self.question_text[:50]


class Answer(models.Model):
    #answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=500)
    is_correct = models.BooleanField(default=True)

    def __str__(self):
        return self.answer_text[:50]
