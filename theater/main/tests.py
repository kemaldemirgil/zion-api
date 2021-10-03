from django.test import TestCase
from .models import Room, Movie, ShowTime


class RoomTest(TestCase):
  def setUp(self):
    Room.objects.create(name='Room-1')
    Room.objects.create(name='roomtwo')

  def test_Room(self):
    """ Rooms that can be created are correctly identified """
    room_1 = Room.objects.get(name='Room-1')
    room_2 = Room.objects.get(name='roomtwo')
    self.assertEqual(
      room_1.__str__(), "Room-1")
    self.assertEqual(
      room_2.__str__(), "roomtwo")

  
class MovieTest(TestCase):
  def setUp(self):
    Movie.objects.create(name='Godfather')
    Movie.objects.create(name='Pulp Fiction')

  def test_Movie(self):
    """ Movies that can be created are correctly identified """
    movie_godfather = Movie.objects.get(name='Godfather')
    movie_pulpfiction = Movie.objects.get(name='Pulp Fiction')
    self.assertEqual(
      movie_godfather.__str__(), "Godfather")
    self.assertEqual(
      movie_pulpfiction.__str__(), "Pulp Fiction")


class ShowTimeTest(TestCase):
  def setUp(self):
    self.movie_name = Movie.objects.create(name="Kill Bill")
    self.room_name = Room.objects.create(name="Room-3")
    self.time = "8.00-11.00"
    self.seats = 4
    
  def test_ShowTime(self):
    """ Show Times that can be created are correctly identified """
    self.assertEqual(self.movie_name.name, "Kill Bill")
    self.assertEqual(self.room_name.name, "Room-3")
    self.assertEqual(self.time, "8.00-11.00")
    self.assertEqual(self.seats, 4)


    