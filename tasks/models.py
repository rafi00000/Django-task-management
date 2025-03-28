from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()

    def __str__(self):
        return self.name

class Task(models.Model):
    status_choices = [
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('C', 'Completed')
    ]
    assigned_to = models.ManyToManyField(Employee)
    project = models.ForeignKey("Project", on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=1, choices=status_choices, default='P')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TaskDetail(models.Model):
    PRIORITY_CHOICES = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low')
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name="details")
    # assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='L')


    def __str__(self):
        return self.priority
    



# signals

@receiver(post_save, sender=Task.assigned_to.through)
def notify_emp_on_task_creation(sender, instance, action , **kwargs):
    if action == "post_add":
        assigned_to_emails = [emp.email for emp in instance.assigned_to.all()]
        send_mail(
            f"New Task Assigned: {instance.title}",
            f"Task Description: \n{instance.description}",
            "rafiul.blf23@gmail.com",
            assigned_to_emails,
            fail_silently=False
        )
