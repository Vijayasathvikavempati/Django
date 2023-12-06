from django.contrib import admin
from django.urls import path
from userapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", views.gethomepage),
    path('user/', views.getnewuserpage),
    path('newemp/', views.getnewemppage),
]
