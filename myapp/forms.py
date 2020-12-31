from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Admin, Officer, Disp, Product
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'location',
                  'is_admin', 'is_officer', 'is_disp', 'password1', 'password2']


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'is_admin', 'is_officer', 'is_disp']


class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
