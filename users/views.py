from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #this is the class
from django.contrib import messages #flash message is imported for error for example message.debug/message.info,etc
from django.contrib.auth.decorators import login_required #this is used to restrict the view file here profile page can be viewed only if the user is logged in
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST': ##if post then create form ,validate and send the data
        form = UserRegisterForm(request.POST)  # instance is created, form that has request.post data from our form
        if form.is_valid():
            form.save() #saving the user to the database
            username = form.cleaned_data.get('username')#'username' is the varible of form used in register.html
            messages.success(request, f'{username} your account has been created! You are able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()   # instance is created empty form
    return render(request, 'users/register.html', {'form': form})

@login_required #this tell the server to run the function below if logged in
def profile(request):
    if request.method == 'POST': #this will activate when we click on the submit buttion
        u_form = UserUpdateForm(request.POST, instance=request.user)#to fill in the current info in the field in profile page
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, #request.FILES is for image file submitted in the form
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():#validate
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'{username} your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)  # to fill in the current info in the field in profile page
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {# dictionary
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)