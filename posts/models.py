from django.db import models

# Create your models here.

class Topics(models.Model):
    title = models.CharField(blank=False, max_length=70)
    sub = models.CharField(blank=False, max_length=200)
    image = models.ImageField(blank=False, upload_to='images/')

class Post(models.Model):
    title = models.CharField(max_length=70)
    sub = models.CharField(max_length=200)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, null=True)
    first = models.TextField(blank=False)
    second = models.TextField(blank=True)
    third = models.TextField(blank=True)
    image = models.ImageField(blank=False, upload_to='images/')
    simage = models.ImageField(null=True, blank=True, upload_to='images/')
    timage = models.ImageField(null=True, blank=True, upload_to='images/')
    date = models.DateField(auto_now_add=False)
    bibliography = models.CharField(max_length=250)