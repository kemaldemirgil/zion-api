from rest_framework import serializers
from main.models import Room, Movie, ShowTime
from drf_writable_nested.serializers import WritableNestedModelSerializer


class RoomSerializer(serializers.ModelSerializer):
    """
    Serializer for Room model
    """

    show_time = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ["name", "show_time"]


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model
    """

    class Meta:
        model = Movie
        fields = "__all__"


class ShowTimeSerializer(WritableNestedModelSerializer):
    """
    Serializer for Showtime model
    """

    movie_name = MovieSerializer(required=False, read_only=False)
    room_name = RoomSerializer(required=False, read_only=False, many=False)

    class Meta:
        model = ShowTime
        fields = ["id", "movie_name", "room_name", "time", "seats"]
