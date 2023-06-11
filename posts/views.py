from django.shortcuts import render, get_object_or_404
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


# def topic_post(request, slug):
#     if (Topics.objects.filter(slug=slug)):
#         post = Post.objects.filter(topic__slug=slug)
#         context={'post':post}
#         return render(request, 'posts/topic_post.html', context)