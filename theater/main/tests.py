from django.test import TestCase
from .models import Room, Movie


class RoomTest(TestCase):
  """ Test module for Room model """

  def setUp(self):
    Room.objects.create(name='Room-1')
    Room.objects.create(name='roomtwo')

  def test_Room(self):
    room_1 = Room.objects.get(name='Room-1')
    room_2 = Room.objects.get(name='roomtwo')
    self.assertEqual(
      room_1.__str__(), "Room-1")
    self.assertEqual(
      room_2.__str__(), "roomtwo")

  
class MovieTest(TestCase):
  """ Test module for Movie model """

  def setUp(self):
    Movie.objects.create(name='Godfather')
    Movie.objects.create(name='Pulp Fiction')

  def test_Movie(self):
    movie_godfather = Movie.objects.get(name='Godfather')
    movie_pulpfiction = Movie.objects.get(name='Pulp Fiction')
    self.assertEqual(
      movie_godfather.__str__(), "Godfather")
    self.assertEqual(
      movie_pulpfiction.__str__(), "Pulp Fiction")
