from django.contrib import admin
from django.urls import path, include
from users.views import home
from users.views import contact_page
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("contact/", contact_page),
    path("task/",include("tasks.urls")),
    path("user/",include("users.urls")),
] + debug_toolbar_urls()