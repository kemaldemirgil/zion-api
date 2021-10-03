from rest_framework import routers
from .api import MovieViewSet, RoomViewSet, ShowTimeViewSet, GetTicketViewSet
from django.urls import include, path


router = routers.DefaultRouter()
router.register('api/movies', MovieViewSet, 'movies')
router.register('api/rooms', RoomViewSet, 'rooms')
router.register('api/showtimes', ShowTimeViewSet, 'showtimes')
router.register('api/get-ticket', GetTicketViewSet, 'tickets')

urlpatterns = [path('', include(router.urls))]