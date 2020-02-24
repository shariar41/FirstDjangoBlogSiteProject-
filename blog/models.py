from django.db import models
from django.utils import timezone #module to modify date
from django.contrib.auth.models import User #this creates an one to many relationship between user/author and post
from django.urls import reverse #alternate to redirect after creating a post


class Post(models.Model):#post class is a table in the db
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)#one to many rel between admin.user table and post(with common attribute author) using foreign key. on_delete=models.CASCADE means if the user is deleted then the post will also be deleted but if post is deleted user will remain

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})#kwargs for specific post with specific pk