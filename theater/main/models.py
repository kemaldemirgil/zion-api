from django.db import models


class Room(models.Model):
  """ Room model """
  name = models.CharField(max_length = 100, null=False)

  def __str__(self):
    return self.name


class Movie(models.Model):
  """ Movie model """
  name = models.CharField(max_length = 100, null=False)

  def __str__(self):
    return self.name


class ShowTime(models.Model):
  """ ShowTime model """
  movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE, null=False)
  room_name = models.ForeignKey(Room, on_delete=models.CASCADE, null=False, related_name="show_time")
  time = models.CharField(max_length = 100, null=False, unique=False)
  seats = models.IntegerField(default=300)

  def __str__(self):
    return f"{self.movie_name} will be playing at {self.time} with {self.seats} capacity."