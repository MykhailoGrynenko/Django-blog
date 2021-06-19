from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserResisterForm


def register(request):
    """If it receives POST request then validate the form data. Otherwise - display the empty form."""
    if request.method != 'POST':
        form = UserResisterForm()
    else:
        form = UserResisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('blog-home')
    return render(request, 'users/register.html', {'form': form})
