from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request,'login_reg/index.html')

def register(request):
    # try:
    if request.method=="POST":
        #if the fields pass the vaildation the  object will be created in the database
        #the registration methhod inside the model, performs all of the checks, creates instances if tests pass and returns True. If there is an error it will return False.
        if User.objects.registration(request):
            context={
                'name':request.POST['first_name'],
                'action': "registered"
            }
            messages.success(request,'Successfully registered')
            return render(request,'login_reg/show.html', context)
        else:
            return redirect('/')
    else:
        return redirect('/')
    # except:
    #     return render(request,'login_reg/error.html')


def login(request):
    # try:
    if request.method=="POST":
        #the login methhod inside the model, performs all of the checks, returns user if tests pass. If there is an error it will return False.
        login=User.objects.login(request)
        if login==False:
            return redirect('/')
        else:
            context={
                'name': login.first_name,
                'action': "logged in"
            }
            messages.success(request,'Successfully logged in')
            return render(request,'login_reg/show.html', context)

    else:
        return redirect('/')
    # except:
    #     return render(request,'login_reg/error.html')
