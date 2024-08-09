"""
URL configuration for sport_events project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for the admin interface
    path('', views.event_list, name='home'),  # Home page displaying the list of events
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),  # Event detail view
    path('event/<int:event_id>/book/', views.book_event, name='book_event'),  # Booking view for an event
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)