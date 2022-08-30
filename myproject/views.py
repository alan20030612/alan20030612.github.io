from ast import Not
from datetime import date
from email import header
from operator import is_
from pickle import NONE
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import web_scraping
from .web_sc import web_sc


# Create your views here.
def index(request):
    web_data = web_scraping.objects.all()
    return render(request, 'index.html', {'web_data': web_data})

# def counter(request):
#     word = request.POST['text']
#     word_counter = len(word.split())
#     return render(request, 'counter.html', {'amount':word_counter})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_config = request.POST['password_config']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already used')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already used')
            return redirect('register')
        if password != password_config:
            messages.info(request, 'Incorrect password configuration')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid information')
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def web_scc(request):
    pages = request.POST.get('pages')
    data = web_sc(pages)
    return render(request, 'web_scc.html', {'data': data})