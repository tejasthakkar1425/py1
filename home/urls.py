from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('about',views.home, name="about"),
    path('contact',views.home, name="contact"),
    path('service',views.home, name="service"),
    path('signin',views.home, name="signin"),
]