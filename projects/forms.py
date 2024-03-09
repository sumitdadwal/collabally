from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        # Iterate over all fields to apply the Bootstrap class
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # For file input, you might want to apply custom classes
            if isinstance(field.widget, forms.ClearableFileInput):
                field.widget.attrs['class'] = 'form-control-file'