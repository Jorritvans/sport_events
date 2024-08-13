from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Model representing an Event
class Event(models.Model):
    title = models.CharField(max_length=200)  # Event title
    description = models.TextField()  # Detailed description of the event
    date = models.DateTimeField()  # Date and time of the event
    location = models.CharField(max_length=200)  # Location of the event
    price = models.DecimalField(
    max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='events/')
    
    def __str__(self):
        return self.title  # String representation of the event


# Model representing a Booking for an event
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Related event
    user = models.CharField(
        max_length=150, blank=True, null=False
    )  # User who booked
    email = models.EmailField()  # Email of the user
    date_booked = models.DateTimeField(default=timezone.now)  # Booking date
    number_of_tickets = models.IntegerField(default=1)  # Number of tickets

    def __str__(self):
        return (
            f"{self.user} booked {self.event.title}"
        )  # String representation


# Model representing a Comment on an event
class Comment(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='comments'
    )  # Related event
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # User who commented
    text = models.TextField()  # Comment text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return (
            f"Comment by {self.user.username} on {self.event.title}"
        )  # String representation