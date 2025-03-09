from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm

# Create your views here.
# work with db
# Transform Data
# Data Pass
# HTTP res / Json res return

def home(req):
    return HttpResponse("Welcome to the task management system home")
    pass

def contact_page(req):
    return HttpResponse("Welcome to contact page")


def sign_up(req):
    if req.method == "GET":
        user_form = RegisterForm()
    if req.method == "POST":
        user_form = RegisterForm(req.POST)
        if user_form.is_valid():
            user_form.save()

    context = {
        "user_form": user_form
    }
    return render(req, "registration/sign_up.html", context)