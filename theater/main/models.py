from django.db import models


class Room(models.Model):
  """ Room model """
  name = models.CharField(max_length = 100, null=False)

  def __str__(self):
    return self.name
