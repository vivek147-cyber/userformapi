from datetime import date
import re
from django.db import models
from django.forms import ValidationError

def validate_phone_number(value):
        if not value.isdigit():
         raise ValidationError("Phone number must contain only digits.")
        if len(value) != 10:
         raise ValidationError("Phone number must be 10 digits long.")
        return value

class UserForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    phone_number = models.CharField(max_length=20,validators=[validate_phone_number])

    

    
