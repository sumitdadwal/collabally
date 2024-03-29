from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from collaborations.models import Profile


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['is_looking_for_collaborator', 'profile_picture'] # Include additional profile fields as needed


