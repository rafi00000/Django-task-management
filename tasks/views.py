from django.http import HttpResponse
from django.shortcuts import render
from tasks.forms import TaskModelForm
from tasks.models import Employee, Task

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
    employees = Employee.objects.all()
    task_form = TaskModelForm()
    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return render(request, 'task_form.html', {'form': task_form, 'message': 'Task created successfully!'})

    context = {
        "form": task_form
    }
    return render(request, "task_form.html", context)
