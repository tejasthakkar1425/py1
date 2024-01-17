from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from home.models import *

def home(request):
    return render(request, "authentication/index.html")

def about(request):
    return render(request, "authentication/about.html")

def contact(request):
    return render(request, "authentication/contact.html")

def service(request):
    return render(request, "authentication/service.html")

def login(request):
    return render(request, "authentication/signin.html")

def stateView(request):
    objStateMaster = state_master_table.objects.all()
    print(objStateMaster)
    return render(request, "authentication/state-list.html",{'stateobj':objStateMaster})

def cityView(request):
    objCityMaster = city_village_master_table.objects.all()
    print(objCityMaster)
    return render(request, "authentication/city-list.html",{'cityobj':objCityMaster})

