from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.home, name="home"),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
