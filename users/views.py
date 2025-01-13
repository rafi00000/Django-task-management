from django.http import HttpResponse
from django.shortcuts import render

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
