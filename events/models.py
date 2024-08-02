from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.name

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number_of_tickets = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.event.name}"