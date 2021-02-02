from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from  django.contrib.auth.hashers import make_password,check_password
from RegistrationApp.models import User
from CandidateApp.models import Candidate

# Create your views here.
def loginn(request):
    return render(request,'voting-window-login.html')

def officer_login_success(request):
    officer_id=request.POST['officer-id']
    password=request.POST['password']
    user=User.objects.get(aadhar_no=officer_id)
    flag=check_password(password,user.password)
    if flag and user.is_voting_officer:
        user=authenticate(username=user.username,password=password)
        print(user)
        login(request,user)
        return redirect('VotingApp:home')
    else:
        return redirect('VotingApp:login')

def home(request):
    return render(request,'voting-window.html')


def officer_logout(request):
    logout(request)
    return redirect('VotingApp:login')

def display_candidates(request):
    more_details=True
    voter_id = request.POST['voting-id']
    user = User.objects.get(voter_id=voter_id)
    print(user)
    pincode = user.pincode[0:3]
    candidates = Candidate.objects.filter(standing_seat_pincode__startswith=pincode)
    print(candidates)
    return render(request,'voting-window.html',{'more_details':more_details, 'candidates':candidates, 'voter_id':voter_id})
