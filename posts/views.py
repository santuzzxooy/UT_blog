from django.shortcuts import render
from posts.models import Post, Topics
from django.views.generic import ListView
# Create your views here.

# def index(request):
#     return render(request,'posts/index.html')

class index(ListView):
    model = Post
    template_name = 'posts/index.html'

class topic(ListView):
    model = Topics
    template_name = 'posts/topics.html'

def about(request):
    return render(request,'posts/about.html')