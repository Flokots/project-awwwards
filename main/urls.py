from django.urls import path
from .views import (
    ProjectListView, 
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView, 
    ProjectDeleteView,
    UserProjectListView,
    add_review,
)
from . import views

urlpatterns=[
    path('', ProjectListView.as_view(), name='index'),
    path('user/<str:username>', UserProjectListView.as_view(), name='user-projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('about/', views.about, name='about'),
    path('search/', views.search_results, name='search_results'),
    path('project/<int:pk>/review/', views.add_review, name='add-review'),
    path('api/project/', views.ProjectList.as_view()),

]

