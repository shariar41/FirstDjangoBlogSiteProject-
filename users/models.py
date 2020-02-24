from django.db import models
from django.contrib.auth.models import  User
from PIL import Image #import image from pillow libarary


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)# this creates an one to one relationship between current user with profile model
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')#profile_pics will be the stored directory when we upload a pic

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)#run the method of our parent class

        img = Image.open(self.image.path)#create an instance of original image

        #max size of image is 125px in our front end project
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)#resize the image to output_size
            img.save(self.image.path)#overwrite the original path
