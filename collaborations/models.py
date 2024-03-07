from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_looking_for_collaborator = models.BooleanField(default=True)
    bio = models.TextField(max_length=500, blank=True)
    # Add other fields like skills, etc if needed.

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    

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
