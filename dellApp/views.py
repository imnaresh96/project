from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.utils import IntegrityError

# Create your views here.
data={}
def index(request):
    return HttpResponse("<h1> This is demo </h1>"),

def signup_page(request):
    return render (request,'signup_page.html')

def signin_page(request):
    return render (request,'signin_page.html')

def forgot_page(request):
    return render (request,'forgot_page.html')

def profile_page(request):
    print(request.POST)
    if 'email' in request.session:
        if load_data(request):
            print('successful')
            return render (request,'profile_page.html')
    print("data not available")
    return redirect (signin_page)


# Signup Functionality
def signup(request):
    print(request.POST)
    # master=Master.objects.all()
    try:
        password=request.POST['password']
        if password==request.POST['confirm_password']:
            Master.objects.create(
                Email=request.POST['email'],
                Password=request.POST['password'],
            )
            print('Registration Succesfully')
            return render(request,'signup_page.html',{'error':'Registration Successfully'})
        else:
            print('both password should be same')
            return render(request,'signup_page.html',{'error':'Both Password Should Be Same'})
    except IntegrityError as err:
        print('Email Already Register')
        return render (request,'signup_page.html',{'error':"Email Already Register"})


#Signin Functionality  
def signin(request):
    print(request.POST)
    try:
        master=Master.objects.get(Email=request.POST['email'])
        if master.Password==request.POST['password']:
            request.session['email']=master.Email
            print('login Successfully')
            return redirect(profile_page)
        else: 
            print('wrong Password')
            return render(request,'signin_page.html',{'error':'Password Does Not Match'})
    except Exception as err:
        print(err)
        return render (request,'signin_page.html',{'error':'Email Not Registerd'})


#load profile data
def load_data(request):
    print(request.POST)     
    master=Master.objects.get(Email=request.session['email'])
    user_profile=User_Profile.objects.get(Master=master)

    user_profile.full_name=User_Profile.FullName
    # user_profile.last_name=User_Profile.FullName.split()[1]
    # user_profile.birthdate=User_Profile.BirthDate.strftime("%Y-%m-%d")
    user_profile.mobile=User_Profile.Mobile
    user_profile.address=User_Profile.Address
    user_profile.gender=User_Profile.Gender

    data['user_data']=user_profile
    