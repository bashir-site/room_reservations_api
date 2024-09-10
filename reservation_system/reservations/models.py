from django.db import models
from django.contrib.auth.models import User


class MeetingRoom(models.Model):
    room_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Meeting Room'
    )
    max_attendees = models.IntegerField(default=5, verbose_name='Meeting Room')

    def __str__(self):
        return self.room_number


class Reservation(models.Model):
    room = models.ForeignKey(
        MeetingRoom,
        on_delete=models.CASCADE,
        verbose_name='Номер переговорки'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Сотрудник'
    )
    start_time = models.DateTimeField(verbose_name='Время начала')
    end_time = models.DateTimeField(verbose_name='Время конца')
    purpose = models.TextField(verbose_name='Цель бронирования')

    class Meta:
        unique_together = ('room', 'start_time', 'end_time')

    def __str__(self):
        return f'{self.user.username} забронировал переговорку - {self.room.room_number}'
