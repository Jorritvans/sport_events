# events/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Booking

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def book_event(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=event_id)
        name = request.POST['name']
        email = request.POST['email']
        number_of_tickets = request.POST['number_of_tickets']
        Booking.objects.create(
            event=event,
            name=name,
            email=email,
            number_of_tickets=number_of_tickets
        )
        return redirect('event_detail', event_id=event_id)