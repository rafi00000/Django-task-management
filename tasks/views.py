from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def show_user_dashboard(request):
    return render(request, 'admin-dashboard.html')

def show_admin_dashboard(request):
    return render(request, 'user-dashboard.html')