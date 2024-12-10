from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
          user = form.save(commit=False)
          user.set_password(form.cleaned_data['password1'])
          user.save()
          login(request, user)
          return redirect('#') # add the url
    else:
        form = UserRegistrationForm()

    return render(request,'registration/register.html',{'form':form})

