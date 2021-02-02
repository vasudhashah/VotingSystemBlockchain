from django.shortcuts import render,redirect
from RegistrationApp.models import *
from django.contrib.auth import authenticate, login, logout
from  django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def login_page(request):
    return render(request,'voter-profile-login.html')

def voter_profile(request):
    user=request.user
    if user.is_authenticated:
        return render(request,'voter-profile.html',{'name':user.full_name,'username':user.username,'voter_id':user.voter_id,'aadhar_no':user.aadhar_no,'phone_no':user.phone_no,'date_of_birth':user.date_of_birth,'age':user.age,'country':user.country,'state':user.state,'city':user.city,'taluka':user.taluka,'pincode':user.pincode,'constituency':user.constituency,'voting_stars':user.voting_stars,'image':user.image})
    else:
        return redirect('VoterProfileApp:login')

def voter_login_success(request):
    voter_id=request.POST['voter-id']
    password=request.POST['password']
    user=User.objects.get(voter_id = voter_id)
    flag=check_password(password,user.password)


    #set_password(password)

    #user = User.objects.get(is_officer=True,aadhar_no=officer_id)

    print(user)
    if flag :
        user=authenticate(username=user.username,password=password)
        print(user)
        login(request,user)
        return redirect('VoterProfileApp:voter-profile')
    else:
        return redirect('VoterProfileApp:login')

def voter_logout(request):
    logout(request)
    return redirect('VoterProfileApp:login')

def changepassword(request):
    return render(request,'changepassword.html')

def changepassword_submit(request):
    user=request.user
    currentpassword=request.POST['currentpassword']
    print(currentpassword)
    newpassword=request.POST['newpassword']
    print(newpassword)
    confirmpassword=request.POST['confirmpassword']
    print(confirmpassword)
    if (newpassword==confirmpassword and check_password(currentpassword,user.password)):

        user = User.objects.filter(aadhar_no = user.aadhar_no).update(password=make_password(newpassword))
        messages.info(request, 'Your password has been changed successfully!')
        return render(request,'changepassword.html')

    messages.info(request, 'Your information doesnot match your profile!')
    return render(request,'changepassword.html')

def forgot_password(request):
    return render(request,'forgot-password.html')

def check_forgot_password(request):
    aadhar_no=request.POST['aadhar_no']
    voter_id=request.POST['voter_id']
    newpassword=request.POST['newpassword']
    user=User.objects.get(aadhar_no = aadhar_no)
    if((user.voter_id==voter_id) & (user.aadhar_no==aadhar_no)):
        user.password = make_password(newpassword)
        mssg="success"
        messages.info(request, 'Your password has been changed successfully!')
        return render(request,'forgot-password.html',{'mssg':mssg})

    mssg="fail"
    messages.info(request, 'Your password and aadhar number does not match!!')
    return render(request,'forgot-password.html',{'mssg':mssg})
