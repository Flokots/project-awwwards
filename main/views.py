from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Project


def index(request):
    title='Home'
    projects= Project.objects.all()
    return render(request, 'index.html', {'title': title, 'projects': projects})


class ProjectListView(ListView):
    model = Project
    template_name = 'index.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-date_posted']

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'

def about(request):
    title='About'
    return render(request, 'about.html', {'title': title})

