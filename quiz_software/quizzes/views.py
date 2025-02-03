from django.shortcuts import render, redirect
from .models import UserProfile, Quiz, Question, Answer
from django.contrib import messages

# Home Page
def home(request):
    users = UserProfile.objects.all()
    return render(request, 'quizzes/home.html', {'users': users})



#What kind of things do I need to add in views?
#Users logging in - would we use django allauth for this?
# Creating, updating, deleting quizzes
#View Quizzes (overview)
#View individual Quiz details
#Results and scores: store and retrieve user scores for quizzes
# Leaderboard (show scores of other users)
#Social sharing & embedding - url generation?

##Admin functionality -> managing users, quizzes, reviewing reports.
