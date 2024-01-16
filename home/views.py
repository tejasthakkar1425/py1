from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "authentication/index.html")

def about(request):
    return render(request, "authentication/about.html")

def contact(request):
    return render(request, "authentication/contact.html")

def service(request):
    return render(request, "authentication/service.html")

def signin(request):
    return render(request, "authentication/signin.html")
