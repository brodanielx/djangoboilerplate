from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message = f'Account created for {username}'
            messages.success(request, message)
            return redirect('home')
    else:
        form = UserRegistrationForm()

    context = {
        'form' : form
    }
    return render(request, 'users/register.html', context)
