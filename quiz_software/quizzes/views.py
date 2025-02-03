from django.shortcuts import render, redirect
from .models import UserProfile, Quiz, Question, Answer
from django.contrib import messages

# Home Page
def home(request):
    users = UserProfile.objects.all()
    return render(request, 'quizzes/home.html', {'users': users})


# Add User


