from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.utils import IntegrityError


# Create your views here.
data={}
data['gender_choice_option']=[]

for k,v in Gender_Choices:
    g={
        'short_k':'k',
        'text':'v',
    }
    data['gender_choice_option'].append(g)

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
        try:
            if load_data(request):
                print('successful')
                return render (request,'profile_page.html',data)
        except Exception as err:
                print("data not available")
                return render (request,'signin_page.html',{'error':'Data Not Available'})
    else:
        return redirect(signin_page)


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
    profile=User_Profile.objects.get(Master=master)

    profile.Image=profile.Image
    profile.first_name=profile.Full_Name.split()[0]
    profile.last_name=profile.Full_Name.split()[1]
    profile.birthdate=profile.BirthDate.strftime("%Y-%m-%d")
    # profile.mobile=profile.Mobile
    # profile.address=profile.Address
    # profile.gender=profile.Gender
    profile.birthdate=profile.birthdate
    # profile.zipcode=profile.zipcode

    data['user_data']=profile
    
    return redirect(profile_page)
    
# # load profile student data
# def profile_data(request):
#     master = Master.objects.get(Email = request.session['email'])
#     profile = User_Profile.objects.get(Master = master)
#     # user_roll=us.objects.get(Common=profile)

#     profile.first_name = profile.Full_Name.split()[0]
#     profile.last_name = profile.Full_Name.split()[1]
#     # user_roll.roll_number = user_roll.Roll_Number
#     profile.BirthDate = profile.BirthDate.strftime("%Y-%m-%d")
#     # profile.DateOfJoining = profile.DateOfJoining.strftime("%Y-%m-%d")

#     data['user_data'] = profile
#     # data['roll_user']=user_roll

#     return redirect(profile_page)

#password reset Functionality
def password_reset(request):
    master=Master.objects.get(Email=request.session['email'])
    if master.Password==request.POST['current_password']:
        if request.POST['new_password']==request.POST['confirm_password']:
            master.Password=request.POST['new_password']
            master.save()
            {'error':'password Change Successfully'}
            print('password Change Successfully')
            # return render(request,'profile_page.html',{'error':'password Change Successfully'})
            return redirect(profile_page)
            
        else:
            {'error':'Both Password Should Be Same'}
            print('Both Password Should Be Same')
            # return render(request,'profile_page.html',{'error':'Both Password Should Be Same'})
            return redirect(profile_page)
    else:
        {'error':'Wrong Current Password'}
        print('Wrong Current Password')
        # return render ({'error':'Wrong Current Password'})
        return redirect(profile_page)

#profile update functionality
def update_data(request):
    master=Master.objects.get(Email=request.session['email'])
    profile=User_Profile.objects.get(Master=master)

    profile.Full_Name=' '.join([request.POST['first_name'],request.POST['last_name']])
    profile.BirthDate=request.POST['birthdate']
    profile.Gender=request.POST['gender']
    profile.Mobile=request.POST['mobile']
    profile.Address=request.POST['address']

    profile.save()
    return redirect(profile_page)


#logout Functionality
def logout(request):
    'email' in request.session
    del request.session['email']
    return redirect(signin_page)
    
# Delete Functionality
def delete_account(request):
    print(request.POST)
    master=Master.objects.get(Email=request.session['email'])
    master.delete()
    return redirect(signin_page)