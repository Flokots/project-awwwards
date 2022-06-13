from django.shortcuts import render, redirect
from django.views.generic import ListView


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

