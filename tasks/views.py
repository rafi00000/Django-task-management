from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def admin_dashboard(request):
    return render(request, 'dashboard/admin-dashboard.html')


def context_req(request):
    context = {
        'names': ['John', 'Doe', 'Jane'],
        'email': 'john@gmail.com',
        'phone': '1234567890',
        'address': '123, Main Street, City, Country'
    }
    return render(request, 'context.html', context)

def create_task(request):
    return render(request, "task_form.html")