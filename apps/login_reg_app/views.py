from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request): #GET
    return render(request, "index.html")

def register(request): 
    # if request.method == 'POST': #POST
    #     errors = User.objects.validator(request.POST)

    #     if len(errors) > 0:
    #         for k, v in errors.items():
    #             messages.error(request, v)
    #         return redirect("/")

    #     else:
    #         pw_hash = bcrypt.hashpw(request.POST['pw_form'].encode(), bcrypt.gensalt()).decode()

    #         print(pw_hash)
            
    #         user = User.objects.create(
    #             first_name=request.POST['firstName_form'], last_name=request.POST['lastName_form'],
    #             email=request.POST['email_form'],
    #             password=pw_hash
    #         ) 

    #         print(user)
    #         request.session['user_id']=user.id 

    #         print(request.POST)
        return redirect("/dashboard")

def login(request): #POST
    #  results = User.objects.filter(email=request.POST['email_form'])

    #  if results: 
    #      logged_user = results[0] 

    #      if bcrypt.checkpw(request.POST['pw_form'].encode(), logged_user.password.encode()):

    #         request.session['user_id'] = logged_user.id
    #         return redirect("/dashboard")
        
    #      else:
    #          messages.error(request, "The email and password do not match.")
    #          return redirect("/") 
    #  else:
    #      messages.error(request, "This email has not been registered.") 
         return redirect("/dashboard") # needs to be just redirect ("/") added /dashboard just for building out html

