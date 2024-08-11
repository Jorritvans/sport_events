# events/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Booking, Comment
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("** This username is already taken **")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("** This email is already registered **")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("** Passwords do not match **")

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'email', 'number_of_tickets']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
