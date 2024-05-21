from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect(settings.SIGNUP_REDIRECT_URL)

    context = {'form': UserCreationForm()}

    return render(request, 'registration/signup.html', context)
