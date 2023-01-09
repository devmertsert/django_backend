from rest_framework import serializers
from django.contrib.auth import authenticate, login
from .models import Movie, WatchList

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id', 'name', 'description', 'image_url', 'language'
            , 'release_date', 'genre', 'imdb'
        )

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = (
            'user', 'movie'
        )