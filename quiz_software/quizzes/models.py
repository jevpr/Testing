from tkinter.constants import CASCADE

from django.db import models

class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=False)
    about = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question_text = models.TextField(max_length=500)
    quiz_id = models.ManyToManyField(Quiz)

    def __str__(self):
        return self.question_text[:50]


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=500)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.answer_text[:50]
