from django.shortcuts import render

from django.views.generic import View
# Create your views here.

def prueba(request):
    return render(request,'posts/index.html')