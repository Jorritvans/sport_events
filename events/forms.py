# events/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Booking, Comment
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'email', 'number_of_tickets']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
