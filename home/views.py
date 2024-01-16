from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# def home(request):
#     return render(request, "authentication/home.html")
class home(TemplateView):
    template_name = "authentication/home.html"

def about(request):
    return render(request, "authentication/about.html")

def contact(request):
    return render(request, "authentication/contact.html")

def service(request):
    return render(request, "authentication/service.html")

def signin(request):
    return render(request, "authentication/signin.html")
