from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import MeetingRoom, Reservation
from rest_framework.test import APIClient


class MeetingRoomTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.token = Token.objects.create(user=self.user)

        self.meeting_room = MeetingRoom.objects.create(
            room_number='Room 101',
            max_attendees=10
        )

    def test_create_meeting_room(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('meetingroom-list'), {
            'room_number': 'Room 102',
            'max_attendees': 5
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MeetingRoom.objects.count(), 2)

    def test_list_meeting_rooms(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('meetingroom-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ReservationTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.token = Token.objects.create(user=self.user)

        self.meeting_room = MeetingRoom.objects.create(
            room_number='Room 101',
            max_attendees=10
        )
        self.reservation = Reservation.objects.create(
            room=self.meeting_room,
            user=self.user,
            start_time='2024-09-01T10:00:00Z',
            end_time='2024-09-01T11:00:00Z',
            purpose='Test Meeting'
        )

    def test_create_reservation(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('reservation-list'), {
            'room': self.meeting_room.id,
            'user': self.user.id,
            'start_time': '2024-09-01T12:00:00Z',
            'end_time': '2024-09-01T13:00:00Z',
            'purpose': 'New Test Meeting'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservation.objects.count(), 2)

    def test_get_reservations_availability(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('reservation-availability'), {
            'room_id': self.meeting_room.id,
            'date': '2024-09-01'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['available'])
