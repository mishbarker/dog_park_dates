from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *

def login(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/signin/login')
        else:
            user = User.objects.get(email = request.POST['email'])
            request.session['user_id'] = user.id
            request.session['user_name'] = user.first_name
            return redirect('/dashboard')
    else:
        return render(request, 'signin.html')
    
def register(request):
    if request.method == "POST":
        errors = User.objects.validate_user(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/signin/register')
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'], password = hashed_password)
        request.session['user_id'] = new_user.id
        request.session['user_name'] = new_user.first_name
        return redirect('/dashboard')
    else:
        return render(request, 'register.html')
def logout(request):
    request.session.flush()
    return redirect('/')

