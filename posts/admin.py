from django.contrib import admin

# Register your models here.
from posts.models import Topics, Post
# Register your models here.

admin.site.register(Topics)
admin.site.register(Post)