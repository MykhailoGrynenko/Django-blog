from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserResisterForm


def register(request):
    """If it receives POST request then validate the form data. Otherwise - display the empty form."""
    if request.method != 'POST':
        form = UserResisterForm()
    else:
        form = UserResisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created. You are now able to log in!")
            return redirect('login')
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """User must be logged in to view the profile page. Otherwise, 404 error occurs.
        Add LOGIN_URL = 'login' in setting.py to redirect to the login page instead."""
    return render(request, 'users/profile.html')