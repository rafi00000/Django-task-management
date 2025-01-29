from django.http import HttpResponse
from django.shortcuts import render
from tasks.forms import TaskForm
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
    task_form = TaskForm(employees=employees) # for get operation by default, also can be declared as: TaskForm(request.GET, employees=employees)
    if request.method == "POST":
        task_form = TaskForm(request.POST, employees=employees)
        if task_form.is_valid():
            data = task_form.cleaned_data
            title = data.get("title")
            description = data.get("description")
            due_date = data.get("due_date")
            assigned_to = data.get("assigned_to") # list of employee ids

            # creating new task
            new_task = Task.objects.create(title=title, description=description, due_date=due_date)
            for emp_id in assigned_to:
                employee = Employee.objects.get(id=emp_id)
                new_task.assigned_to.add(employee)
                return HttpResponse("Task created successfully")


    context = {
        "form": task_form
    }
    return render(request, "task_form.html", context)
