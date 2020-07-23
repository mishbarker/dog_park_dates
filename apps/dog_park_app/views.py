from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def logout(request): #POST 
    # request.session.flush()
    return redirect("/")

def dashboard(request): #GET
    # if "user_id" not in request.session:
    #     return redirect("/")
    # else:
    #     context = {
    #         "all_trips": Trip.objects.all().order_by('-created_by'),
    #         "user": User.objects.get(id=request.session['user_id']),
    #     }
        return render(request, 'all_trips.html', context)

def new(request): #GET
    # context = {
    #         "user": User.objects.get(id=request.session['user_id']),
    #     }
    return render(request, 'new.html', context)

def create(request): #POST
    # if request.method == 'POST':
    #     errors = Trip.objects.validator(request.POST)
    #     if len(errors) > 0:
    #         for k, v in errors.items():
    #             messages.error(request, v)
        
    #     if len(messages.get_messages(request)) > 0:
    #         return redirect("/new")

    #     else:
    #         user = User.objects.get(id=request.session["user_id"])
    #         trip = Trip.objects.create(
    #             destination = request.POST['destination_form'], 
    #             start_date = request.POST['start_date_form'], 
    #             end_date = request.POST['end_date_form'], 
    #             plan = request.POST['plan_form'], 
    #             user = user
    #         )
    #         print(trip.destination)
    #         print(trip.start_date)
    #         print(trip.end_date)
    #         print(trip.plan)
            
            return redirect(f'/show_one/{trip.id}')

def show_one(request): #GET, id

    # context = {
    #     "user": User.objects.get(id=request.session['user_id']),
    #     "trip": Trip.objects.get(id=id),
    # }
    return render(request, 'show_one.html', context)

def edit(request): # , id
    # trip = Trip.objects.get(id=id)
    # trip.start_date = str(trip.start_date)
    # trip.end_date = str(trip.end_date)
    # context = {
    #     "user": User.objects.get(id=request.session['user_id']),
    #     "trip": trip,
    # }
    return render(request, 'edit.html', context)

def update(request): # , id
    # if request.method == 'POST':

    #     trip = Trip.objects.get(id=id)

    #     errors = Trip.objects.validator(request.POST)

    #     if len(errors) > 0:
    #         for k, v in errors.items():
    #             messages.error(request, v)
    #         return redirect(f'/edit/{trip.id}')

    #     else:
    #         trip = Trip.objects.get(id=id)
    #         trip.destination = request.POST['destination_form']
    #         trip.start_date = request.POST['start_date_form']
    #         trip.end_date = request.POST['end_date_form']
    #         trip.plan = request.POST['plan_form']
    #         trip.save()
        return redirect('/dashboard')

def remove(request): # , id
    # trip = Trip.objects.get(id=id)
    # if trip.user.id == request.session['user_id']:
    #     trip.delete()
    return redirect('/dashboard')