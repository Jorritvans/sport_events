# events/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='event_images/', default='path/to/default_image.jpg')

    def __str__(self):
        return self.title

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.CharField(max_length=150, blank=True, null=False)
    email = models.EmailField()
    date_booked = models.DateTimeField(default=timezone.now)
    number_of_tickets = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user} booked {self.event.title}"

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.event.title}"
