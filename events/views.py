from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Event, Booking, Comment
from .forms import RegisterForm, BookingForm, CommentForm

# View for listing all events on the home page
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})

# View for displaying details of a specific event
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    comments = event.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.user = request.user
            comment.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = CommentForm()
    return render(request, 'events/event_detail.html', {'event': event, 'comments': comments, 'form': form})

# View for booking an event (login required)
@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        user = request.user
        email = user.email
        number_of_tickets = request.POST.get('number_of_tickets')

        if number_of_tickets:
            Booking.objects.create(
                event=event,
                user=user.username,
                email=email,
                number_of_tickets=number_of_tickets
            )
            return render(request, 'events/success.html')
    return render(request, 'events/book_event.html', {'event': event})

# View for displaying a message if login is required to access a page
def login_required_view(request):
    return render(request, 'events/login_required.html')

# View for displaying the user's bookings (login required)
@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user.username)
    return render(request, 'events/user_bookings.html', {'bookings': bookings})

# View for editing a specific booking (login required)
@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user.username)
    if request.method == 'POST':
        booking.number_of_tickets = request.POST.get('number_of_tickets')
        booking.save()
        return redirect('user_bookings')
    return render(request, 'events/edit_booking.html', {'booking': booking})

# View for canceling a specific booking (login required)
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user.username)
    if request.method == 'POST':
        booking.delete()
        return redirect('user_bookings')
    return render(request, 'events/cancel_booking.html', {'booking': booking})

# View for registering a new user
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'events/register.html', {'form': form})

# View for logging in a user
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'events/login.html', {'form': form})

# View for logging out a user
def logout_view(request):
    logout(request)
    return redirect('home')

# View for displaying the about page
def about(request):
    return render(request, 'events/about.html')

# View for displaying the contact page
def contact(request):
    return render(request, 'events/contact.html')
