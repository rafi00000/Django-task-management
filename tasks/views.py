from django.http import HttpResponse
from django.shortcuts import render, redirect
from tasks.forms import TaskModelForm, TaskDetailModelForm
from tasks.models import Employee, Task, TaskDetail
from datetime import date
from django.db.models import Count, Q
from django.contrib import messages

# Create your views here.

def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def admin_dashboard(request):
    # data retrieval from the database
    all_tasks = Task.objects.select_related("details").all()

    counts = Task.objects.aggregate(
        total_task= Count("id"),
        pending_task= Count("id", filter=Q(status="P")),
        completed_task= Count("id", filter=Q(status="C")),
        in_progress_task= Count("id", filter=Q(status="I"))
    )

    # conditionally retrieve all tasks from the database    
    type = request.GET.get("type")
    if type == "completed":
        all_tasks = Task.objects.filter(status="C")
    elif type == "pending":
        all_tasks = Task.objects.filter(status="P")
    elif type == "in_progress":
        all_tasks = Task.objects.filter(status="I")

    context = {
        "counts": counts,
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
    task_form = TaskModelForm()
    task_detail_form = TaskDetailModelForm()

    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            messages.success(request, "Task created successfully")
            return redirect("create-task")

    context = {
        "task_form": task_form,
        "task_detail_form": task_detail_form
    }
    return render(request, "task_form.html", context)

def update_task(request, id):
    print("Update id: ", id)
    old_task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=old_task)
    task_detail_form = TaskDetailModelForm(instance=old_task)

    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            messages.success(request, "Task created successfully")
            return redirect("create-task")

    context = {
        "task_form": task_form,
        "task_detail_form": task_detail_form
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