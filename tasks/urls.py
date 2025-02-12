from django.urls import path
from tasks.views import user_dashboard, admin_dashboard, context_req, create_task, view_tasks, update_task

urlpatterns = [
    path("user-dashboard/", user_dashboard),
    path("admin-dashboard/", admin_dashboard, name="admin-dashboard"),
    path("context/", context_req),
    path("create-task/", create_task, name="create-task"),
    path("view-tasks/", view_tasks),
    path("update-task/<int:id>/", update_task, name="update-task")
]