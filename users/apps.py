from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): #to create profile for every users without going to admin and change profile pic of the users. Automatically create the profile here pic
        import users.signals