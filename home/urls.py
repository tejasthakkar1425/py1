from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "home"

urlpatterns = [
    path('',views.home, name="home"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('service',views.service, name="service"),
    path('login',views.login, name="login"),
    path('stateView',views.stateView,name="stateView"),
    path('cityView',views.cityView,name="cityView"),
    path('gstView',views.gstView,name='gstView'),
    path('distView',views.distView,name="cityView"),
    path('docView',views.docView,name="docView"),
    path('vehViwe',views.vehViwe,name="vehViwe"),
    path('vehroutViwe',views.vehroutViwe,name="vehroutViwe"),
    path('userView',views.userView,name="userView"),
    path('reviewView',views.reviewView,name="reviewView"),
]