from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from apps.login_reg_app.models import User
import urllib.request
import json

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    if "user_id" not in request.session:
        return redirect('/signin/login')
    else:
        context = {
            'all_playdates': Playdate.objects.order_by("-created_at"),
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'dashboard.html', context)

def new(request):
    if "user_id" in request.session:
        context={
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
        if request.method == "POST":
            errors = Playdate.objects.validate_playdate(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)
                return redirect('/playdates/new')
            else: 
                user = User.objects.get(id=request.session["user_id"])
                Playdate.objects.create(
                    park_name = request.POST['park_name'],
                    address = request.POST['address'],
                    date = request.POST['date'],
                    time = request.POST['time'],
                    comments = request.POST['comments'],
                    creator = user
                )
                return redirect('/dashboard')
        return render(request, 'new.html', context)            
    return redirect('/')
        

    

def delete_playdate(request, id):
    playdate = Playdate.objects.get(id=id)
    playdate.delete()
    return redirect('/dashboard')

def show_one(request, id):
    if "user_id" not in request.session:
        return redirect('/')
    else:
        playdate = Playdate.objects.get(id=id)
        creator_id = playdate.creator.id
        dog = Dog.objects.get(owner=User.objects.get(id=creator_id))
        owner = dog.owner.first_name
        print(owner)
        context = {
            'dog': Dog.objects.get(owner=User.objects.get(id=creator_id)),
            'logged_user': User.objects.get(id=request.session['user_id']),
            'viewed_playdate': Playdate.objects.get(id=id),
            'users_joined': playdate.users_who_joined.all()
        }
    return render(request, 'show_one.html', context)

def edit_playdate(request, id):
    if "user_id" in request.session:
        playdate = Playdate.objects.get(id=id)
        playdate.date = str(playdate.date)
        playdate.time = str(playdate.time)
        context = {
            'dog': Dog.objects.get(owner=User.objects.get(id=request.session['user_id'])),
            'edit_playdate': playdate,
            'logged_user': User.objects.get(id=request.session['user_id']),
        }
        if request.method == "POST":
            errors = Playdate.objects.validate_playdate(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)
                return redirect(f'/playdates/edit/{id}')
            edit_playdate= Playdate.objects.get(id=id)
            edit_playdate.park_name = request.POST['park_name']
            edit_playdate.address = request.POST['address']
            edit_playdate.date = request.POST['date']
            edit_playdate.time = request.POST['time']
            edit_playdate.comments = request.POST['comments']
            edit_playdate.save()
            return redirect('/dashboard')
        return render(request, 'edit.html', context)
    return redirect('/')
    
def join(request, playdate_id):
    playdate_to_join = Playdate.objects.get(id=playdate_id)
    logged_user = User.objects.get(id=request.session['user_id'])
    playdate_to_join.users_who_joined.add(logged_user)
    return redirect('/dashboard')

def un_join(request, playdate_id):
    cancel_joined_playdate = Playdate.objects.get(id=playdate_id)
    logged_user = User.objects.get(id=request.session['user_id'])
    cancel_joined_playdate.users_who_joined.remove(logged_user)
    return redirect('/dashboard')
    
def profile(request):
    if 'user_id' in request.session:
        context ={
        'user': User.objects.get(id=request.session['user_id']),
        'dog': Dog.objects.get(owner=User.objects.get(id=request.session['user_id']))
        }
        return render(request, 'profile.html', context)
    return redirect('/')

def create_dog(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            Dog.objects.create( owner=User.objects.get(id=request.session['user_id']), name=request.POST['dog_name'], breed=request.POST['breed'], gender=request.POST['gender'], image=request.FILES['image'])
            return redirect('/users/profile')
        return render(request, 'new_dog.html')
    return redirect('/')


# def edit_profile(request):
#     if 'user_id' in request.session:
#         if request.method == 'POST':
#             errors = User.objects.validate_profile_user(request.POST, request.session['id'])
#             if len(errors) > 0:
#                 for key, value in errors.items():
#                     messages.error(request, value)
#                 return redirect('/users/profile')
#             user = User.objects.get(id=request.session['id'])
#             user.first_name = request.POST['first_name']
#             user.last_name = request.POST['last_name']
#             user.email = request.POST['email']
#             hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
#             user.password = hashed_password
#             user.save()
#             return redirect('/users/profile')
#         return render(request, 'profile.html', context)
#     return redirect('/')


