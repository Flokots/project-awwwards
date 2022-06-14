from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Project
from users.models import Profile



def index(request):
    title='Home'
    projects= Project.objects.all()
    return render(request, 'index.html', {'title': title, 'projects': projects})


class ProjectListView(ListView):
    model = Project
    template_name = 'index.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-date_posted']
    paginate_by = 3


class UserProjectListView(ListView):
    model = Project
    template_name = 'main/user_projects.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(developer=user).order_by('-date_posted')


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
    success_url = '/'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.developer:
            return True
        return False



def about(request):
    title='About'
    return render(request, 'about.html', {'title': title})


def search_results(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        searched_projects = Project.search_by_title(search_term)

        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'projects': searched_projects})

    else:
        message = "You haven't searched for any project"

        return render(request, 'search.html', {'message': message})

