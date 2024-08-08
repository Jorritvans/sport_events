from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Booking

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def book_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        user = request.POST.get('user')
        email = request.POST.get('email')
        number_of_tickets = request.POST.get('number_of_tickets')

        if user and email and number_of_tickets:
            Booking.objects.create(
                event=event,
                user=user,
                email=email,
                number_of_tickets=number_of_tickets
            )
            return render(request, 'events/success.html')
    return render(request, 'events/book_event.html', {'event': event})

def booking_success(request):
    return render(request, 'events/booking_success.html')

def about(request):
    return render(request, 'events/about.html')

def contact(request):
    return render(request, 'events/contact.html')