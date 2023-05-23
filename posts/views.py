from django.shortcuts import render
from models import Post
from django.views.generic import ListView
# Create your views here.

class index(ListView):
    model = Post
    template_name = 'posts/index.html'

def about(request):
    return render(request,'posts/about.html')