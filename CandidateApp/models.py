from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, Group
from django.core.validators import MinValueValidator,ValidationError
from datetime import date
from  django.contrib.auth.hashers import make_password,check_password
from RegistrationApp.models import *

class Candidate(models.Model):
    user = models.ForeignKey('RegistrationApp.User', on_delete = models.CASCADE)
    party = models.CharField(max_length=100, null=True)
    standing_seat_pincode = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username+self.user.aadhar_no+"_"+self.party
