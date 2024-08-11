from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Model representing an event
class Event(models.Model):
    title = models.CharField(max_length=200)  # Event title
    description = models.TextField()  # Detailed description of the event
    date = models.DateTimeField()  # Date and time of the event
    location = models.CharField(max_length=200)  # Location of the event
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the event
    image = models.ImageField(upload_to='event_images/', default='path/to/default_image.jpg')  # Image associated with the event

    def __str__(self):
        return self.title  # String representation of the event

# Model representing a booking for an event
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Event that is being booked
    user = models.CharField(max_length=150, blank=True, null=False)  # User who booked the event
    email = models.EmailField()  # Email of the user who booked the event
    date_booked = models.DateTimeField(default=timezone.now)  # Date and time when the booking was made
    number_of_tickets = models.IntegerField(default=1)  # Number of tickets booked

    def __str__(self):
        return f"{self.user} booked {self.event.title}"  # String representation of the booking

# Model representing a comment on an event
class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')  # Event associated with the comment
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who made the comment
    text = models.TextField()  # Content of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time when the comment was created

    def __str__(self):
        return f"Comment by {self.user.username} on {self.event.title}"  # String representation of the comment
