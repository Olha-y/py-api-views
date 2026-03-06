from rest_framework import serializers

from cinema.models import Actor, Genre, CinemaHall, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["first_name", "last_name"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["name", "rows", "seats_in_row"]


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["title", "description", "duration", "actors", "genres"]
