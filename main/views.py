from django.shortcuts import render, redirect
from django.views.generic import ListView


def index(request):
    title='Home'
    return render(request, 'index.html', {'title': title})

def about(request):
    title='About'
    return render(request, 'about.html', {'title': title})

