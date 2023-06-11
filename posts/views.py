from django.shortcuts import render
from posts.models import Post, Topics
from django.views.generic import ListView
# Create your views here.
from .decorators import PageTitleMixin

# def index(request):
#     return render(request,'posts/index.html')

class index(PageTitleMixin, ListView):
    model = Post
    page_title = 'Home'
    template_name = 'posts/index.html'

class topic(PageTitleMixin, ListView):
    model = Topics
    page_title = 'Topics'
    template_name = 'posts/topics.html'

def about(request):
    page_title = 'About'
    return render(request,'posts/about.html',{
                  'page_title':page_title})


def topic_post(request, title):
    if (Topics.objects.filter(title=title)):
        post = Post.objects.filter(topic__title=title)
        context={'post':post}
        return render(request, 'posts/topic_post.html', context)