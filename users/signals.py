from django.db.models.signals import post_save #this a signal that get fired after an object is saved
from django.contrib.auth.models import User
from django.dispatch import receiver #a function that gets this signal and the perform some tasks
from .models import Profile


@receiver(post_save, sender=User)# when a user is saved then send this (post_save) signal to be recieved by the reciever here it is create_profile function
def create_profile(sender, instance, created, **kwargs): #the reciever create_profile takes all the arguments i.e sender, instance of the user) signals sent by post_save
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)# when a user is saved then send this (post_save) signal to be recieved by the reciever here it is create_profile function
def save_profile(sender, instance, **kwargs): #the reciever create_profile takes all the arguments i.e sender, instance of the user) signals sent by post_save
    instance.profile.save()
