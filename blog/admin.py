#super username: Saimon pass:Shariar41
from django.contrib import admin
from .models import Post

admin.site.register(Post)#this allows you to add post data from db to admin gui or panel
