from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserResisterForm(UserCreationForm):
    """Add additional required email field."""
    email = forms.EmailField()  # default required=True

    class Meta:
        """Specify model that will interact with the form and fields that will be shown on the form."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        """A user can update username and email fields."""
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        """A user can update image field."""
        model = Profile
        fields = ['image']
