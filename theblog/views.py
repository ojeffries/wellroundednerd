from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'



