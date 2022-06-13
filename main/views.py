from pyexpat import model
from typing import List
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Project


def index(request):
    title='Home'
    projects= Project.objects.all()
    return render(request, 'index.html', {'title': title, 'projects': projects})


class ProjectListView(ListView):
    model = Project

def about(request):
    title='About'
    return render(request, 'about.html', {'title': title})

