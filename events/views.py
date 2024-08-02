from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Booking

# View for displaying the list of events
def event_list(request):
    # Retrieve all events from the database
    events = Event.objects.all()
    # Render the events in the template
    return render(request, 'events/home.html', {'events': events})

# View for displaying details of a specific event
def event_detail(request, event_id):
    # Retrieve the event with the given ID
    event = get_object_or_404(Event, pk=event_id)
    # Render the event details in the template
    return render(request, 'events/event_detail.html', {'event': event})

# View for handling event bookings
def book_event(request, event_id):
    # If the request method is POST, process the booking
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=event_id)
        name = request.POST['name']
        email = request.POST['email']
        number_of_tickets = request.POST['number_of_tickets']
        # Create a new booking in the database
        Booking.objects.create(
            event=event,
            name=name,
            email=email,
            number_of_tickets=number_of_tickets
        )
        # Redirect to the event details page
        return redirect('event_detail', event_id=event_id)
