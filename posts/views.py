from django.shortcuts import render

from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

def prueba(request):
    return HttpResponse("Esto es una prueba")