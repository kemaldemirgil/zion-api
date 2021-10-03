from main.models import Movie, Room, ShowTime
from rest_framework import viewsets, permissions
from .serializers import MovieSerializer, RoomSerializer, ShowTimeSerializer
from rest_framework.response import Response


class MovieViewSet(viewsets.ModelViewSet):
  """ View set for Movie model"""
  queryset = Movie.objects.all()
  permission_classes = [ permissions.AllowAny ]
  serializer_class = MovieSerializer


class RoomViewSet(viewsets.ModelViewSet):
  """ View set for Room model"""
  queryset = Room.objects.all()
  permission_classes = [ permissions.AllowAny ]
  serializer_class = RoomSerializer

  def get_queryset(self):
    lookup_key = self.request.query_params.get('name', None)
    if lookup_key:
      queryset = self.queryset.filter(name=lookup_key)
      return queryset
    return Room.objects.all()

  
class ShowTimeViewSet(viewsets.ModelViewSet):
  """ View set for Show Time model"""
  queryset = ShowTime.objects.all()
  permission_classes = [ permissions.AllowAny ]
  serializer_class = ShowTimeSerializer


class GetTicketViewSet(viewsets.ModelViewSet):
  """ View set for Get Ticket request"""
  queryset = ShowTime.objects.all()
  permission_classes = [ permissions.AllowAny ]
  serializer_class = ShowTimeSerializer  

  def list(self, request):
    serializer = ShowTimeSerializer(self.queryset, many=False)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    if pk:
      queryset = ShowTime.objects.get(id=pk)
      queryset.seats = int(queryset.seats) - 1
      queryset.save()
      serializer = ShowTimeSerializer(queryset, many=False)
      return Response(serializer.data)