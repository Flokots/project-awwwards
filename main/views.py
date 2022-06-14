from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
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

    def form_valid(self, form):
        form.instance.developer = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'landing_page', 'description', 'link']

    def form_valid(self, form):
        form.instance.developer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.developer:
            return True
        return False


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'project_detail.html'


    def test_func(self):
        project = self.get_object()
        if self.request.user == project.developer:
            return True
        return False



def about(request):
    title='About'
    return render(request, 'about.html', {'title': title})

