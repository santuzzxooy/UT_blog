from django.urls import path    
import views

urlpatterns = [
    path('', views.prueba, name='prueba')
]