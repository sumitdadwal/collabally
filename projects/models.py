from django.db import models
from collaborations.models import Profile

# Create your models here.
class ProjectType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_type = models.ForeignKey(ProjectType, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_looking_for = models.CharField(max_length=255) # Description of the collaborator they are looking for

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f'Image for project: {self.project.title}'
    