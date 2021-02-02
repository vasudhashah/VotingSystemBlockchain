from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from  django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('RegistrationApp:user_register_window')
    else:
        return redirect('RegistrationApp:login')

def user_register_window(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST, request.FILES)

		if form.is_valid():

			form.save()
			return redirect('RegistrationApp:success')
	else:
		form = RegistrationForm()
	return render(request, 'registration-home1.html', {'form' : form})

def success(request):
	return HttpResponse('successfully uploaded')

def officer_login_success(request):
    officer_id=request.POST['officer-id']
    password=request.POST['password']
    user=User.objects.get(aadhar_no=officer_id)
    flag=check_password(password,user.password)
    print(user)
    if flag and user.is_officer:
        user=authenticate(username=user.username,password=password)
        print(user)
        login(request,user)
        return redirect('RegistrationApp:home')
    else:
        return redirect('RegistrationApp:login')

def officer_logout(request):
    logout(request)
    return redirect('RegistrationApp:login')


def user_register_success(request):
    full_name = request.POST.get('full-name',False)
    aadhar_no = request.POST.get('aadhar-no',False)
    date_of_birth = request.POST.get('dob',False)
    phone_no = int(request.POST.get('phone-no',False))
    country = request.POST.get('country',False)
    state = request.POST.get('state',False)
    city = request.POST.get('city',False)
    taluka = request.POST.get('taluka',False)
    pincode= request.POST.get('pincode',False)
    constituency= request.POST.get('constituency',False)
    profile_pic = request.POST['image']

    user_obj = User.objects.create(
    username="_".join(full_name.split(" ")),
    full_name=full_name,
    aadhar_no=aadhar_no,
    date_of_birth=date_of_birth,
    phone_no=phone_no,
    country=country,
    state=state,
    city=city,
    taluka=taluka,
    pincode=pincode,
    constituency=constituency,
    image=profile_pic
    )
    user_obj.save()
    return render(request,'ex.html',{'voterId':user_obj.voter_id,'aadhar_no':user_obj.aadhar_no,'image':user_obj.image})

def login_window(request):
    return render(request,'registration-login.html')

def update_window(request):
    update_flag=False
    return render(request,'update.html',{'update_flag':update_flag})

def ok(request):
    aadhar_no = request.POST['aadhar-no']
    user=User.objects.get(aadhar_no=aadhar_no)
    update_flag=True
    return render(request,'update.html',{'user':user, 'update_flag':update_flag})

def save_update_details(request):
    aadhar_no = request.FILES['aadhar-no']
    full_name = request.POST.get('full-name')
    date_of_birth = request.POST.get('dob')
    phone_no = int(request.POST.get('phone-no'))
    country = request.POST.get('country')
    state = request.POST.get('state')
    city = request.POST.get('city')
    taluka = request.POST.get('taluka')

    user = User.objects.filter(aadhar_no = aadhar_no).update(full_name=full_name,date_of_birth=date_of_birth,phone_no=phone_no,country=country,state=state,city=city,taluka=taluka)

    return redirect('RegistrationApp:home')
