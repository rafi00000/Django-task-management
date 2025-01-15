from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def admin_dashboard(request):
    return render(request, 'dashboard/admin-dashboard.html')

