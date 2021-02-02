from django.shortcuts import render
from RegistrationApp.models import *
from .models import *
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from  django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def ec_login(request):
    return render(request,'ec-login.html')

def ec_login_success(request):
    ec_officer_id=request.POST['ec-officer-id']
    password=request.POST['password']
    user=User.objects.get(aadhar_no=ec_officer_id)
    flag=check_password(password,user.password)
    print(user)
    if flag and user.is_ec_officer:
        user=authenticate(username=user.username,password=password)
        print(user)
        login(request,user)
        return redirect('CandidateApp:ec-home')
    else:
        return redirect('CandidateApp:ec-login')

def ec_home(request):
    if request.user.is_authenticated:
        return render(request,'ec-home.html')
    else:
        return redirect('CandidateApp:ec-login')

def ec_logout(request):
    logout(request)
    return redirect('CryptoBallotsHomeApp:home')

def candidate_register_home(request):
    if request.user.is_authenticated:
        return render(request, 'candidate-register-home.html')
    else:
        return redirect('CandidateApp:ec-login')

def candidate_register_success(request):
    if request.user.is_authenticated:
        aadhar_no = request.POST['aadhar-no']
        party = request.POST['party']
        standing_seat_pincode = request.POST['standing-pincode']
        user=User.objects.get(aadhar_no=aadhar_no)
        candidate = Candidate.objects.create(
        user=user,
        party=party,
        standing_seat_pincode=standing_seat_pincode
        )
        candidate.save()
        return redirect('CandidateApp:candidate-register-home')
    else:
        return redirect('CandidateApp:ec-login')
