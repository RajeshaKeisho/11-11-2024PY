print("Importing UserRegistrationForm in views.py")

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm
from django.contrib import messages
from django.views.decorators.http import require_POST


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'profiles/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return redirect('profile').url  # Redirect to the profile page after login

@login_required
def profile(request):
    return render(request, 'profiles/profile.html')


@require_POST
@login_required
def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')  # Redirect to the login page
