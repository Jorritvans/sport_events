from django.urls import path
from . import views

# URL patterns for the events application
urlpatterns = [
    path('', views.event_list, name='home'),  # Home page showing the list of events
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),  # Detailed view of a specific event
    path('event/<int:event_id>/book/', views.book_event, name='book_event'),  # Booking form for a specific event
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('register/', views.register, name='register'),  # User registration page
    path('login/', views.login_view, name='login'),  # User login page
    path('logout/', views.logout_view, name='logout'),  # User logout
    path('bookings/', views.user_bookings, name='user_bookings'),  # User's bookings page
    path('bookings/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),  # Edit a booking
    path('bookings/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),  # Cancel a booking
    path('login-required/', views.login_required_view, name='login_required'),  # Login required message
]
