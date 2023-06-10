from django.db import models
from django.utils.text import slugify

# Create your models here.

class Topics(models.Model):
    title = models.CharField(blank=False,
                             max_length=70)
    
    sub = models.CharField(blank=False,
                           max_length=200)
    
    image = models.ImageField(blank=False,
                              upload_to='images/')

    slug = models.SlugField(max_length=255,
                            blank=True,
                            null=True,
                            unique=True)

    def __str__(self):
        return self.title
    
        # OBTENER UN SLUG UNICO
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Topics.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, *kwargs)

    

class Post(models.Model):
    title = models.CharField(max_length=70)
    sub = models.CharField(max_length=200, default='*')
    year = models.CharField(max_length=10)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, null=True)
    first = models.TextField(blank=False)
    second = models.TextField(blank=True)
    third = models.TextField(blank=True)
    image = models.ImageField(blank=False, upload_to='images/')
    simage = models.ImageField(null=True, blank=True, upload_to='images/')
    timage = models.ImageField(null=True, blank=True, upload_to='images/')
    date = models.DateField(auto_now_add=False)
    bibliography = models.CharField(max_length=250)
    url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title