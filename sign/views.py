# from django.shortcuts import redirect, render

# Create your views here.
from inspect import ismethoddescriptor
from multiprocessing import AuthenticationError
from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.contrib.auth.models import User ,auth
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import auth 
# from django.contrib.auth import views as auth_views 
from django.contrib import messages
# from studentstudyportal import settings
# from django.core.mail import send_mail

# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['pwd']

        if User.objects.filter(username=username).exists():
            # print("user taken")
            messages.error(request,f"Username Taken")
            # messages.info(request,"Username Taken")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            print("email taken")
            # messages.info(request,"email taken")
            messages.error(request,f"Email Taken")
            return redirect('signup')
        else:
            user =User.objects.create_user(username=username,email=email,password=pwd)
            user.save()

        #    Welcome msg email
            # subject="welcome to our site"
            # message="hello   {username} " 
            # from_email=settings.EMAIL_HOST_USER
            # to_list={user.email}
            # send_mail(subject,message,from_email,to_list,fail_silently=True)

            # print("user created")
            messages.success(request,f"Account Created for {username} succesfully  !!")
            return redirect('signin')
    else:
        return render(request,'sign/signup.html')

def signin(request):
    if request.method=="POST":
        # username=request.POST['username']
        username=request.POST['username']
        pwd=request.POST['pwd']

        user=authenticate(username=username,password=pwd)

        if user is not None:
            # auth.login(request,user)
            login(request,user)
            
            return redirect('/')
        else:
            messages.error(request,"Invalid User")
            return redirect('signin')
    else:
        return render(request,'sign/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged out succesfully")
    return redirect('/')