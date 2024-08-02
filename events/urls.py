from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='home'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/book/', views.book_event, name='book_event'),
]