from django.urls import path
from tasks.views import user_dashboard, admin_dashboard, context_req, create_task, view_tasks

urlpatterns = [
    path("user-dashboard/", user_dashboard),
    path("admin-dashboard/", admin_dashboard),
    path("context/", context_req),
    path("create-task/", create_task),
    path("view-tasks/", view_tasks)
]