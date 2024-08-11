from django.contrib import admin
from .models import Event, Booking, Comment


# Admin configuration for the Event model
class EventAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('title', 'date', 'location', 'price')

    # Fields to search in the admin list view
    search_fields = ('title', 'location')


# Admin configuration for the Booking model
class BookingAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = (
        'event', 'user', 'email',
        'date_booked', 'number_of_tickets'
    )

    # Fields to search in the admin list view
    search_fields = ('event__title', 'user__username')


# Admin configuration for the Comment model
class CommentAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('event', 'user', 'created_at', 'text')

    # Fields to search in the admin list view
    search_fields = ('event__title', 'user__username')


# Register the models with the Django admin site
admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Comment, CommentAdmin)
