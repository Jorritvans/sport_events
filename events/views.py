from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Event, Booking, Comment
from .forms import RegisterForm, BookingForm, CommentForm


# View to list all events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})


# View to show event details and handle comments
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
    return render(
        request, 'events/event_detail.html',
        {'event': event, 'comments': comments, 'form': form}
    )


# View to handle event booking
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


# View to display a login required message
def login_required_view(request):
    return render(request, 'events/login_required.html')


# View to list all bookings for a logged-in user
@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user.username)
    return render(
        request, 'events/user_bookings.html',
        {'bookings': bookings}
    )


# View to edit a booking
@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(
        Booking, pk=booking_id, user=request.user.username
    )
    if request.method == 'POST':
        booking.number_of_tickets = request.POST.get('number_of_tickets')
        booking.save()
        return redirect('user_bookings')
    return render(request, 'events/edit_booking.html', {'booking': booking})


# View to cancel a booking
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(
        Booking, pk=booking_id, user=request.user.username
    )
    if request.method == 'POST':
        booking.delete()
        return redirect('user_bookings')
    return render(request, 'events/cancel_booking.html', {'booking': booking})


# View to handle user registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, 'Your account has been created successfully!'
            )
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'events/register.html', {'form': form})


# View to handle user login
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


# View to handle user logout
def logout_view(request):
    logout(request)
    return redirect('home')


# View to display the About page
def about(request):
    return render(request, 'events/about.html')


# View to display the Contact page
def contact(request):
    return render(request, 'events/contact.html')


# View to edit a comment
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=comment.event.id)
    else:
        form = CommentForm(instance=comment)
    return render(
        request, 'events/edit_comment.html',
        {'form': form, 'comment': comment}
    )


# View to delete a comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    event_id = comment.event.id
    if request.method == 'POST':
        comment.delete()
        return redirect('event_detail', event_id=event_id)
    return render(request, 'events/delete_comment.html', {'comment': comment})
