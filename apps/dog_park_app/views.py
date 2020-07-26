from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    pass
    return render(request, 'index.html')

def dashboard(request):
    if "user_id" not in request.session:
        return redirect('/signin/login')
    else:
        context = {
            'all_playdates': Playdate.objects.order_by("-created_at"),
            'user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'dashboard.html', context)

def new(request):
    if "user_id" in request.session:
        if request.method == "POST":
            errors = Playdate.objects.validate_playdate(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)
                return redirect('/playdates/new')
            else: 
                user = User.objects.get(id=request.session["user_id"])
                playdate = Playdate.objects.create(
                    park_name = request.POST['park_name'],
                    address = request.POST['address'],
                    date = request.POST['date'],
                    time = request.POST['time'],
                    comments = request.POST['comments'],
                    creator = user
                )
                return redirect('/dashboard')
        return render(request, 'new.html')            
    return redirect('/')
        

    

def delete_playdate(request, id):
    playdate = Playdate.objects.get(id=id)
    playdate.delete()
    return redirect('/dashboard')

def show_one(request, id):
    if "user_id" not in request.session:
        return redirect('/')
    else:
        context = {
            'logged_user': User.objects.get(id=request.session['user_id']),
            'viewed_playdate': Playdate.objects.get(id=id)
        }
    return render(request, 'show_one.html', context)

def edit_playdate(request, id):
    if "user_id" in request.session:
        hello = Playdate.objects.get(id=id)
        hello.date = str(hello.date)
        hello.time = str(hello.time)
        context = {
            'edit_playdate': hello,
            'logged_user': User.objects.get(id=request.session['user_id'])
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
    
    




    # return render(request, 'index.html')
