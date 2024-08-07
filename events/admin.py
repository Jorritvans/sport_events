from django.contrib import admin
from .models import Event, Booking

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'price')
    search_fields = ('title', 'location')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'email', 'date_booked', 'number_of_tickets')  # Corrected list_display
    search_fields = ('event__title', 'user__username')

admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
