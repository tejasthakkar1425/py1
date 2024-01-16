from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from home.views import home

urlpatterns = [
    path('',home.as_view(), name="home"),
    path('about',views.home, name="about"),
    path('contact',views.home, name="contact"),
    path('service',views.home, name="service"),
    path('signin',views.home, name="signin"),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
