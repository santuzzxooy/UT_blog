from django.shortcuts import render

from django.views.generic import View
# Create your views here.

def index(request):
    return render(request,'posts/index.html')

def about(request):
    return render(request,'posts/about.html')