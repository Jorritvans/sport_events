from django.contrib import admin
from .models import Event, Booking

# Registering the Event and Booking models with the admin site
admin.site.register(Event)
admin.site.register(Booking)