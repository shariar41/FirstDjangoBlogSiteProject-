from django import forms
from django.contrib.auth.models import User #import user model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm): #UserRegisterForm inherits the UserCreationForm
    email = forms.EmailField() #add new user created field

    class Meta:# this class tells about the affected model,fields,etc that you want to edit
        model = User #it says model named User is affected
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # add new user created field

    class Meta:  # this class tells about the affected model,fields,etc that you want to edit
        model = User  # it says model named User is affected
        fields = ['username', 'email'] #this allows you to update/work with username,email field of the current user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:  # this class tells about the affected model,fields,etc that you want to edit
        model = Profile  # it says model named User is affected
        fields = ['image']