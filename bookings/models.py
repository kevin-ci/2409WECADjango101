from django.db import models
from django.contrib.auth.models import User

class Profession(models.Model):
    profession = models.CharField(max_length=100)

    def __str__(self):
        return self.profession

class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings", blank=True, null=True,
    )
    doctor_type = models.ForeignKey(
        Profession, on_delete=models.CASCADE, related_name="bookings", blank=True, null=True,
    )
    date = models.DateField()
    time = models.TimeField()
    booked = models.BooleanField(default=False)
