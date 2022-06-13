from django.shortcuts import render, redirect
from .models import Project

def index(request):
    title='Home'
    projects= Project.objects.all()
    return render(request, 'index.html', {'title': title, 'projects': projects})

def about(request):
    title='About'
    return render(request, 'about.html', {'title': title})

