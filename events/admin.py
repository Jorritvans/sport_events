from django.contrib import admin
from .models import Event, Booking
from .models import Contact

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'price')
    search_fields = ('title', 'location')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'email', 'date_booked', 'number_of_tickets')
    search_fields = ('event__title', 'user__username')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')

admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Contact, ContactAdmin)
