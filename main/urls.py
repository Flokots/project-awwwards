from django.urls import path
from .views import (
    ProjectListView, 
    ProjectDetailView,
    ProjectCreateView,
)
from . import views

urlpatterns=[
    path('', ProjectListView.as_view(), name='index'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('about/', views.about, name='about'),
]

