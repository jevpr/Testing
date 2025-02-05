from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Quiz, Question, Answer

# Home Page
def home(request):
    users = User.objects.all()
    return render(request, 'quizzes/home.html', {'users': users})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "quizzes/register.html", {"form":form})


#What kind of things do I need to add in views?
#Users logging in - would we use django allauth for this?
#
# Creating, updating, deleting quizzes
#View Quizzes (overview)
#View individual Quiz details
#Results and scores: store and retrieve user scores for quizzes
# Leaderboard (show scores of other users)
#Social sharing & embedding - url generation?

##Admin functionality -> managing users, quizzes, reviewing reports.
#Check if the user has the right access before any operation is carried out (otherwise, redirected to log in page)
#Finish controller (views and urls) by the end of this week
#AullAuth research - installation, quickstart