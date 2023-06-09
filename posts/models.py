from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=70)
    sub = models.CharField(max_length=200)
    first = models.TextField(blank=False)
    second = models.TextField(blank=True)
    third = models.TextField(blank=True)
    image = models.ImageField(blank=False, upload_to='images/')
    simage = models.ImageField(null=True, blank=True, upload_to='images/')
    timage = models.ImageField(null=True, blank=True, upload_to='images/')
    date = models.DateField(auto_now_add=False)
    bibliography = models.CharField(max_length=250)