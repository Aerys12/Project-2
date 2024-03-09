# This file is used to create a form for user registration.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
        help_texts = {
            'username': None,
        }
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        error_messages = {
            'username': {
                'unique': 'A user with that username already exists'
            },
            'email': {
                'unique': 'This email is already exists',
                'invalid': 'Enter a valid email address',
            },
            'password1': {
                'min_length': 'This password is too short. It must contain at least 8 characters', 
            },
            'password2': {
                'password_mismatch': 'The two password fields didn’t match',
            }
        }


        
       
