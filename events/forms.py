from django import forms
from .models import Booking, ContactSubmission

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'email', 'number_of_tickets']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']