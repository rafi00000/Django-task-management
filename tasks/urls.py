from django.urls import path
from tasks.views import show_user_dashboard, show_admin_dashboard

urlpatterns = [
    path("show-user-dashboard/", show_user_dashboard),
    path("show-admin-dashboard/", show_admin_dashboard),
]