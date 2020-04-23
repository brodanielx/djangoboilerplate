from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileUpdateForm, UserRegistrationForm, UserUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message = f'{username}, your account has been created! You are now able to login.'
            messages.success(request, message)
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {
        'form' : form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):

    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()

    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }

    return render(request, 'users/profile.html', context)
