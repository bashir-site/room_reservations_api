from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MeetingRoomViewSet, ReservationViewSet


router = DefaultRouter()
router.register(r'meeting-rooms', MeetingRoomViewSet)
router.register(r'reservations', ReservationViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
