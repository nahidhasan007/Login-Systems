from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy

def login(request):

    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("Successfully Logged in")
            return redirect("success")
        else:
            print("invalid credintials")
            return redirect("login")
    else:
        print("Please Try Again")
        return render(request,'login_system/login.html')



def register(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        email = request.POST.get('email')
        
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        print("user created")
        return redirect("success1")
    
    else:
        print("Try again")
        return render(request,'login_system/register.html')

def success(request):
    return render(request,'login_system/success.html')

def success1(request):
    return render(request,'login_system/success1.html')

