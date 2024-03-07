from django.shortcuts import render, redirect
from .forms import UserCreateForm, ProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login




def user_signup(request):
    if request.method == "POST":
        user_form = UserCreateForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user # Link profile to newly created user
            profile.save()
            return redirect('user-login') # Redirect to login page after sign-up
        
    else:
        user_form = UserCreateForm()
        profile_form = ProfileForm()
    return render(request, 'collaborations/signup.html', {'user_form':user_form, 'profile_form':profile_form})
    

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('profile_page') # Redirect to a profile page or home page after login
        else:
            return render(request, 'collaborations/login.html', {'error': 'Invalid username or password.'})
        
    else:
        return render(request, 'collaborations/login.html')

