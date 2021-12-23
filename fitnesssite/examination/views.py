from django.shortcuts import render,HttpResponse
from django.views.generic import ListView

from .models import *

def home(request):
    return render(request, 'training/home.html', {'title': 'Home page'})

def about(request):
    return render(request, 'training/about.html', {'title': 'About'})

def examination(request):
    return render(request, 'training/examination.html', {'title': 'Examination'})


class Examination_page(ListView):
    model = Examination
    template_name = 'training/examination.html'

def login(request):
    return render(request, 'training/login.html', {'title': 'Sign in'})

def register(request):
    return render(request, 'training/register.html', {'title': 'Sign up'})


