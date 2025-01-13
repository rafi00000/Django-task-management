from django.contrib import admin
from django.urls import path, include
from users.views import home
from users.views import contact_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("contact/", contact_page),
    path("",include("tasks.urls"))
]