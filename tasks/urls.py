from django.urls import path
from tasks.views import user_dashboard, admin_dashboard, context_req

urlpatterns = [
    path("user-dashboard/", user_dashboard),
    path("admin-dashboard/", admin_dashboard),
    path("context/", context_req)
]