from django.shortcuts import render, redirect
from .forms import UserCreateForm, ProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Profile
from projects.models import Project
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required




def user_signup(request):
    if request.method == "POST":
        user_form = UserCreateForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
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
            return redirect('user-profile_view') # Redirect to a profile page or home page after login
        else:
            return render(request, 'collaborations/login.html', {'error': 'Invalid username or password.'})
        
    else:
        return render(request, 'collaborations/login.html')
    
@login_required
def profile_view(request):
    profile = request.user.profile
    projects = Project.objects.filter(creator=request.user.profile)
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid() and request.user.profile.is_looking_for_a_collaborator:
            new_project = form.save(commit=False)
            new_project.creator = request.user.profile
            new_project.save()
            return redirect('user-profile_view')
    context = {
        'profile': request.user.profile,
        'projects':projects,
        'form': form,
        'is_collaborator': not request.user.profile.is_looking_for_collaborator,
    }
    return render(request, 'collaborations/profile.html', context)



