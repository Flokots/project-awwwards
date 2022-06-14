from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView
)
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


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'landing_page', 'description', 'link']
    template_name = 'project_form.html'

    def form_valid(self, form):
        form.instance.developer = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['title', 'landing_page', 'description', 'link']
    template_name = 'project_form.html'

    def form_valid(self, form):
        form.instance.developer = self.request.user
        return super().form_valid(form)

def about(request):
    title='About'
    return render(request, 'about.html', {'title': title})

