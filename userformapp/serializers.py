# in your app's serializers.py file
from datetime import date
import re
from rest_framework import serializers
from .models import UserForm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm
        fields = ['name', 'email', 'gender','dob', 'phone_number']


    def validate_dob(self, dob):
        age = (date.today() - dob).days // 365
        if age < 18:
            raise serializers.ValidationError("You must be 18 years or older to register.")
        return dob

    
