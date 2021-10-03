from django.test import TestCase
from .models import Room, Movie, ShowTime
from rest_framework import status
from rest_framework.test import APITestCase


class RoomTest(TestCase):
  def setUp(self):
    Room.objects.create(name='Room-1')
    Room.objects.create(name='roomtwo')

  def test_Room(self):
    """ 
    Room __str__ returns back correctly.
    """
    room_1 = Room.objects.get(name='Room-1')
    room_2 = Room.objects.get(name='roomtwo')
    self.assertEqual(
      room_1.__str__(), "Room-1")
    self.assertEqual(
      room_2.__str__(), "roomtwo")

    with self.assertRaises(Exception):
      self.assertEqual(room_1.__str__(), "Some other room")
  

  
class MovieTest(TestCase):
  def setUp(self):
    Movie.objects.create(name='Godfather')
    Movie.objects.create(name='Pulp Fiction')

  def test_Movie(self):
    """ 
    Movies __str__ returns back correctly.
    """
    movie_godfather = Movie.objects.get(name='Godfather')
    movie_pulpfiction = Movie.objects.get(name='Pulp Fiction')
    self.assertEqual(
      movie_godfather.__str__(), "Godfather")
    self.assertEqual(
      movie_pulpfiction.__str__(), "Pulp Fiction")
    
    with self.assertRaises(Exception):
      self.assertEqual(movie_godfather.__str__(), "Some other movie")
    


class ShowTimeTest(TestCase):
  def setUp(self):
    self.movie_name = Movie.objects.create(name="Kill Bill")
    self.room_name = Room.objects.create(name="Room-3")
    self.time = "8.00-11.00"
    self.seats = 4
    
  def test_ShowTime(self):
    """ 
    Show Times that can be created are correctly identified 
    """
    self.assertEqual(self.movie_name.name, "Kill Bill")
    self.assertEqual(self.room_name.name, "Room-3")
    self.assertEqual(self.time, "8.00-11.00")
    self.assertEqual(self.seats, 4)

    with self.assertRaises(Exception):
      self.assertEqual(self.movie_name.name, "Some other movie")


class RoomTests(APITestCase):
  def test_create_room(self):
    """
    Ensure we can create a new room object.
    """
    url = ('/api/rooms/')
    data = {'name': 'Room-1'}
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Room.objects.count(), 1)
    self.assertEqual(Room.objects.get().name, 'Room-1')

    with self.assertRaises(Exception):
      self.assertEqual(Room.objects.get().name, 'Some other room')


class SingleRoomTest(APITestCase):
  def setUp(self):
    ShowTime.objects.create(
      movie_name=Movie.objects.create(name="Kill Bill"), 
      room_name=Room.objects.create(name="Room-1"),
      time = "8.00-11.00",
    )
    ShowTime.objects.create(
      movie_name=Movie.objects.create(name="Matrix"), 
      room_name=Room.objects.create(name="Room-1"),
      time = "12.00-15.00",
    )
    ShowTime.objects.create(
      movie_name=Movie.objects.create(name="Terminator"), 
      room_name=Room.objects.create(name="Room-2"),
      time = "16.00-19.00",
    )
  
  def test_create_room(self):
    """
    Ensure we can get a single room
    """
    url = ('/api/rooms/?name=Room-2')
    response = self.client.get(url, follow=True)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(Room.objects.filter(name="Room-2").count(), 1)

    with self.assertRaises(Exception):
      self.assertEqual(Room.objects.filter(name="Room-2").count(), 4)


class TicketTests(APITestCase):
  def setUp(self):
    ShowTime.objects.create(
      movie_name=Movie.objects.create(name="Kill Bill"), 
      room_name=Room.objects.create(name="Room-3"),
      time = "8.00-11.00",
      seats = 200
    )

  def test_create_ticket(self):
    """
    Ensure we can create a new ticket object.
    """
    url = ('/api/get-ticket/1')
    response = self.client.get(url, follow=True)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(ShowTime.objects.get().seats, 199)

    with self.assertRaises(Exception):
      self.assertEqual(ShowTime.objects.get().seats, 200)