from django.http import HttpResponse
from django.shortcuts import render
from tasks.forms import TaskModelForm
from tasks.models import Employee, Task, TaskDetail
from datetime import date

# Create your views here.

def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def admin_dashboard(request):
    # data retrieval from the database
    total_task = Task.objects.all().count()
    pending_task = Task.objects.filter(status="P").count()
    completed_task = Task.objects.filter(status="C").count()
    in_progress_task = Task.objects.filter(status="I").count()
    all_tasks = Task.objects.select_related("details").all()

    context = {
        "total_task": total_task,
        "pending_task": pending_task,
        "completed_task": completed_task,
        "task_in_progress": in_progress_task,
        "all_tasks": all_tasks
    }
    return render(request, 'dashboard/admin-dashboard.html', context)


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


# def view_tasks(request):
#     # retrieve all tasks from the database
#     task = Task.objects.all()

#     #retrieve a specific task from the database
#     single_task = Task.objects.get(id=1)

#     # filter tasks based on a specific condition
#     pending_tasks = Task.objects.filter(status="P")
#     due_today = Task.objects.filter(due_date=date.today())
#     """Show the task whose priority is not low / only high and medium """
#     high_medium_priority = TaskDetail.objects.exclude(priority="L")

#     # show the task using contains. It is case-insensitive
#     itask = Task.objects.filter(title__icontains="dev")
#     context = {
#         "tasks": task,
#         "single_task": single_task,
#         "pending_tasks": pending_tasks,
#         "today_due": due_today,
#         "high_medium_priority": high_medium_priority,
#         "itask": itask
#     }
#     return render(request, "view_task.html", context)


def view_tasks(request):
    # select_related query
    tasks = Task.objects.select_related("employee").all()
    context = {
        "tasks": tasks
    }
    return render(request, "view_task.html", context)