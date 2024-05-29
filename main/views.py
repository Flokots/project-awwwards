from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .serializer import ProjectSerializer
from django.shortcuts import render
from .models import Project, Review


def index(request):
    title = 'Home'
    projects = Project.objects.all()
    return render(request, 'index.html', {'title': title, 'projects': projects})


class ProjectListView(ListView):
    model = Project
    template_name = 'index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-date_posted']
    paginate_by = 3


class UserProjectListView(ListView):
    model = Project
    template_name = 'main/user_projects.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(developer=user).order_by('-date_posted')


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['reviews'] = project.reviews.all()
        context['average_design_rating'] = project.average_design_rating()
        context['average_usability_rating'] = project.average_usability_rating()
        context['average_content_rating'] = project.average_content_rating()
        context['average_rating'] = project.average_rating()
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'link', 'description', 'landing_page']

    def form_valid(self, form):
        form.instance.developer = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'link', 'description', 'landing_page']

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
    title = 'About'
    return render(request, 'about.html', {'title': title})


def search_results(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        searched_projects = Project.search_by_title(search_term)

        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'projects': searched_projects})

    else:
        message = "You haven't searched for any project"

        return render(request, 'search.html', {'message': message})


class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)


class ProjectAddReview(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['design_rating', 'usability_rating', 'content_rating', 'comment']
    template_name = 'add_review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get('project_id')
        context['project'] = get_object_or_404(Project, id=project_id)
        return context

    def form_valid(self, form):
        # Get the project by ID from the URL
        project_id = self.kwargs['project_id']
        project = get_object_or_404(Project, id=project_id)

        # Set the user and project before saving the form
        form.instance.user = self.request.user
        form.instance.project = project

        # Save the form
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the project detail page after successful review submission
        return reverse_lazy('project-detail', kwargs={'pk': self.kwargs['project_id']})
