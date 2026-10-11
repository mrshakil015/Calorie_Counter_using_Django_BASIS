from django.contrib.auth.models import User
from calorie_counter_app.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = '__all__'
        exclude = ['user','bmr']

class ConsumedCalorieForm(forms.ModelForm):
    class Meta:
        model = ConsumedCalorieModel
        fields = '__all__'
        exclude = ['user']