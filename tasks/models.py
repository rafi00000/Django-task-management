from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()

class Task(models.Model):
    assigned_to = models.ManyToManyField(Employee)
    project = models.ForeignKey("Project", on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TaskDetail(models.Model):
    PRIORITY_CHOICES = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low')
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='L')