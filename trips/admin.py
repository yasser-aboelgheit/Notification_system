from django.contrib import admin
from .models import Trip, PassengerTrip, Station


admin.site.register(Trip)
admin.site.register(PassengerTrip)
admin.site.register(Station)
