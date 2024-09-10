from django.contrib import admin
from .models import MeetingRoom, Reservation

# Register your models here.
admin.site.register(MeetingRoom)
admin.site.register(Reservation)
