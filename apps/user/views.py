# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import *
import bcrypt


def index(request):
    return render(request, 'user/index.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if len(user) > 0:
        is_pass = bcrypt.checkpw(password.encode('utf-8'), user[0].password.encode('utf-8'))
        if is_pass:
            request.session['id'] = user[0].id
            return redirect('/dashboard')
        else:
            messages.error(request, "Incorrect email and/or password")
            return redirect('/login-page')
    else:
        messages.error(request, "User does not exist")
    return redirect('/login-page')

def register(request):
    errors = User.objects.validate_user(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/register-page')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=hashed_pw)
        return redirect('/login-page')

def logout(request):
    request.session.clear()
    return redirect('/')

def register_page(request):
    form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, 'user/register-page.html', context)

def login_page(request):
    form = LoginForm()
    context = {
        "form": form
    }
    return render(request, 'user/login-page.html', context)

def dashboard(request):
    user = User.objects.get(id=request.session['id'])
    users = User.objects.all()
    context = {
        "user": user,
        "users": users,
    }
    return render(request, 'user/dashboard.html', context)

def profile(request, id):
    user = User.objects.get(id=id)
    messages = Message.objects.filter(user=user)
    context = {
        "user": user,
        "message": messages,
    }
    return render(request, 'user/profile.html', context)

def delete_user(request, id):
    item = User.objects.get(id=id)
    item.delete()
    messages.success(request, 'User deleted successfully!')
    return redirect('/dashboard')

def process_message(request, id):
    errors = Message.objects.validate_message(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/')
    else:
        user_to = User.objects.get(id=id)
        user = User.objects.get(id=request.session['id'])
        body = request.POST['body']
        Message.objects.create(user_to=user_to, user=user, body=body)
        messages.success(request, 'Successfully added message')
        return redirect('/dashboard')
