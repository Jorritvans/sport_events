from django.db import models

# Model representing an event
class Event(models.Model):
    # Name of the event
    name = models.CharField(max_length=100)

    # Detailed description of the event
    description = models.TextField()

    # Date and time when the event will occur
    date = models.DateTimeField()

    # Location where the event will be held
    location = models.CharField(max_length=100)

    # Image associated with the event
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.name

# Model representing a booking for an event
class Booking(models.Model):
    # Event associated with the booking
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    # Name of the person making the booking
    name = models.CharField(max_length=100)

    # Email of the person making the booking
    email = models.EmailField()

    # Number of tickets booked
    number_of_tickets = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.event.name}"
