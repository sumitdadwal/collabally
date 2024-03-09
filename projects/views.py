from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Project, ProjectImage
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


@login_required
def create_project(request):
    # Note: ImageFormSet is not used in this revised approach but kept for reference or future use.
    ImageFormSet = modelformset_factory(ProjectImage, fields=('image',), extra=3, max_num=10)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        # This line is not needed for handling multiple images through a single input
        # formset = ImageFormSet(request.POST, request.FILES, queryset=ProjectImage.objects.none())

        if form.is_valid():  # Removed formset.is_valid() check for simplicity
            project = form.save(commit=False)
            project.creator = request.user.profile
            
            # Check if the profile is looking for a collaborator before saving
            if not project.creator.is_looking_for_collaborator:
                return HttpResponseForbidden("You are not allowed to create a project.")
            
            project.save()

            # Handling multiple images uploaded through a single input field named 'project_images'
            images = request.FILES.getlist('project_images')  # Make sure this matches your input field's name
            for image in images:
                ProjectImage.objects.create(project=project, image=image)
            
            return redirect('collaborations:user-profile_view')
    else:
        form = ProjectForm()
        # Initial formset declaration is kept in case you want to use it elsewhere
        formset = ImageFormSet(queryset=ProjectImage.objects.none())
    # Updated context to not include formset if not used in template
    return render(request, 'projects/create_project.html', {'form': form})




