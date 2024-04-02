from django.contrib.auth import logout, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    template_name = 'app2/login.html'
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect('retrieve_url')
        else:
            return HttpResponse('pz enter correct credentials')
    return render(request, template_name)


@login_required(login_url='login_url')
def logout_view(request):
    logout(request)
    return redirect('signup_url')


def signup_view(request):
    template_name = 'app2/signup.html'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registration Success')
    return render(request, template_name, context={'form': form})

