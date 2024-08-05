from django.contrib import admin
from .models import Event, Booking

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'price')
    search_fields = ('title', 'location')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'email', 'number_of_tickets', 'date_booked')
    search_fields = ('event__title', 'name', 'email')

admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
