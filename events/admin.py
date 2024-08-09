from django.contrib import admin
from .models import Event, Booking, Comment

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'price')
    search_fields = ('title', 'location')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'email', 'date_booked', 'number_of_tickets')
    search_fields = ('event__title', 'user__username')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'created_at', 'text')
    search_fields = ('event__title', 'user__username')

admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Comment, CommentAdmin)