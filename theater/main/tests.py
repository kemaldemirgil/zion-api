from django.test import TestCase
from .models import Room


class RoomTest(TestCase):
  """ Test module for Room model """

  def setUp(self):
    Room.objects.create(name='Room-1')
    Room.objects.create(name='Room-2')

  def test_Room(self):
    room_1 = Room.objects.get(name='Room-1')
    room_2 = Room.objects.get(name='Room-2')
    self.assertEqual(
      room_1.__str__(), "Room-1")
    self.assertEqual(
      room_2.__str__(), "Room-2")
