from django.db import models
from django.contrib.auth.models import User
from accounts.models import Driver, Passenger


class Station(models.Model):
    """
    Model to save bus stops, this is supposed to use GPS coordinates but to save time
    we used names
    """
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Trip(models.Model):
    """Trip model which is created """

    driver = models.ForeignKey(
        Driver, related_name="%(app_label)s_%(class)s_related", on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    failed_attempts = models.IntegerField(null=False, default=0)
    stations = models.ManyToManyField(Station, related_name="%(app_label)s_%(class)s_related", blank=True)
    number_of_seats = models.IntegerField()
    available_seats = models.IntegerField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if self._state.adding is True:
            self.available_seats = self.number_of_seats
        return super(Trip, self).save(*args, **kwargs)


class PassengerTrip(models.Model):
    """Passenger model for passenger users"""
    passenger = models.ForeignKey(Driver, related_name="%(app_label)s_%(class)s_related", on_delete=models.CASCADE)
    work_address = models.CharField(max_length=128)
    trip =  models.ForeignKey(Trip, related_name="%(app_label)s_%(class)s_related", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
