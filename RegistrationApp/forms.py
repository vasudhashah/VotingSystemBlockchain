from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image','full_name','aadhar_no','date_of_birth','age','phone_no','country','state','city','taluka','pincode','constituency']
