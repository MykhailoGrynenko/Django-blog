from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserResisterForm(UserCreationForm):
    """Add additional required email field."""
    email = forms.EmailField()  # default required=True

    class Meta:
        """Specify model that will interact with the form and fields that will be shown on the form."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']
