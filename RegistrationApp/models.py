from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, Group
from django.core.validators import MinValueValidator,ValidationError
from random import randint
from datetime import date
from  django.contrib.auth.hashers import make_password,check_password
import hashlib
import time
def aadhar_check(aadhar_no):
    if len(aadhar_no)!=12 :
        return ValidationError('Aadhar Number is wrong')
    else:
        return aadhar_no

def phone_check(phone_no):
    if len(str(phone_no))!=10 :
        return ValidationError('Phone Number is wrong')
    else:
        return phone_no

def user_directory_path(instance,filename):
    print('aa raha hai')
    return 'profile_pic_{0}_{1}'.format(instance.username,filename)

class User(AbstractUser):
    image=models.ImageField(upload_to='images/',null=True)
    full_name = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=100,validators=[aadhar_check], default='000000000000')
    date_of_birth = models.CharField(null=True,max_length=12,default='0000-00-00')
    #date_of_birth=str(date_of_birth)
    age = models.IntegerField( null=True, blank=True)
    phone_no = models.IntegerField(validators=[phone_check], default=0000000000)
    country = models.CharField( max_length=100, null=True)
    state = models.CharField( max_length=100, null=True)
    city = models.CharField( max_length=100, null=True)
    taluka = models.CharField( max_length=100, null=True)
    pincode = models.CharField( max_length=100, null=True)
    constituency = models.CharField(max_length=100, null=True)

    voting_stars = models.FloatField(default=0.0)
    voter_id = models.CharField( max_length=100,null=True, blank=True)
    is_officer = models.BooleanField(default=False)
    is_ec_officer = models.BooleanField(default=False)
    is_voting_officer = models.BooleanField(default=False)

    def calculateAge(birthDate):
        today = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age

    def save(self,*args,**kwargs):
        self.username="_".join(self.full_name.split(" "))
        self.full_name=self.full_name.capitalize()
        today = date.today()

        self.age = today.year - int(self.date_of_birth[0:4]) - ((today.month, today.day) < (int(self.date_of_birth[5:7]), int(self.date_of_birth[8:10])))
        #self.age = calculateAge(())
        s=str(self.aadhar_no)+str(self.aadhar_no)[::-1]
        self.voter_id = str(int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16)%10**8)


        self.voter_id = self.full_name[0:2]+self.voter_id
        print('voterid',self.voter_id)
        self.password = self.voter_id
        self.password=make_password(self.password)
        #self.set_password(self.password)
        print('age',self.age)
        super().save(*args,**kwargs)
#Ka66242877


    def __str__(self):
        return self.username+self.aadhar_no

# Create your models here.
'''
class UserManager(BaseUserManager):
    def create_user(self,full_name,aadhar_no,date_of_birth,phone_no,country,state,city,taluka,voting_stars=0,voter_id="0000000000",is_officer=False,age=0,password=None):
        if not date_of_birth:
            raise ValueError("User must have an date_of_birth")
        if not aadhar_no:
            raise ValueError("User must have a Aadhar Card")
        if not country:
            raise ValueError("User must have a country")
        if not state:
            raise ValueError("User must have an state")
        if not city:
            raise ValueError("User must have a city")
        if not taluka:
            raise ValueError("User must have Taluka")
        if not phone_no:
            raise ValueError(" User must have a mobile number")

        user_obj = self.model(
        full_name=full_name,
        aadhar_no=aadhar_no,
        voter_id = full_name[0:2]+str(int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16)%10**8),
        date_of_birth=date_of_birth,
        phone_no=phone_no,
        country=country,
        state=state,
        city=city,
        taluka=taluka
        )
        password=0
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,full_name,aadhar_no,password):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")
        if not aadhar_no:
            raise ValueError("User must have an aadhar_no")

        user = self.create_user(
            email=email.lower(),
            full_name = full_name,
            aadhar_no = aadhar_no,
            password = password
        )


        user.admin = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
'''
