from random import choice

from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import Otp


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
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password')
            em = form.cleaned_data.get('email')
            user = User.objects.create_user(username=un, password=pw, email=em, is_active=False)
            otp = ''
            L = [str(i) for i in range(0, 10)]
            for i in range(4):
                otp += choice(L)
            send_mail('otp', f'YOUR OTP IS = {otp}', 'tanujarbhong@gmail.com', [user.email])
            otp = Otp(user=user, otp=int(otp))
            otp.save()
            return redirect('otp_url')
    return render(request, template_name, context={'form': form})


def otp_view(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        otp = request.POST.get('otp')
        print(334)
        try:
            user = User.objects.get(username=un)
            if user.check_password(pw):
                otp = Otp.objects.get(user=user, otp=otp)
                # print( otp )
                if otp:
                    user.is_active = True
                    user.save()
                    return redirect('login_url')
        except:
            return HttpResponse('Something went wrong...!')

    template = 'app1/otp.html'
    context = {}
    return render(request, template, context)
