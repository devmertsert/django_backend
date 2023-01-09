from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import LoginSerializer, MovieSerializer, WatchlistSerializer
from .helpers import jwt_encode_handler
from .models import User, Movie, WatchList

# Create your views here.
class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        userExists = User.objects.filter(email=serializer.validated_data['email']).exists()
        user = None
        
        if userExists:
            user = User.objects.get(email=serializer.validated_data['email'])
            if user.password != serializer.validated_data['password']:
                user = None

        if not user:
            response = {
                'status': False,
                'message': 'Bilgiler geçersiz',
            }
            
            return Response(response, status=400)

        payload = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role
        }

        response = {
            'status': True,
            'message': 'Giriş başarılı',
            'user': {
                'id': user.id,
                'name': user.name
            }
        }

        token = jwt_encode_handler(payload)
        response['token'] = token
        
        return Response(response, status=200)

class MoviesAPIView(APIView):
    
    def get(self, request, movie_id=None):
        
        if movie_id:
            movies = Movie.objects.filter(id=movie_id)
        else:
            movies = Movie.objects.all()
        
        serializer = MovieSerializer(movies, many=True)
        movies = serializer.data
        
        response = {
            'status': True,
            'message': 'Filmler başarıyla getirildi',
            'data': {
                'movies': movies
            }
        }
        
        return Response(response, status=200)

class WatchlistAPIView(APIView):

    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if WatchList.objects.filter(**request.data).exists():
            response = {
                'status': False,
                'message': 'Bu film listenizde mevcut',
            }
            
            return Response(response, status=400)
        
        serializer.save()

        response = {
            'status': True,
            'message': 'Film, listenize başarıyla eklendi'
        }

        return Response(response, status=201)
    
    def delete(self, request):
        serializer = WatchlistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if WatchList.objects.filter(**request.data).exists():
            watchList = WatchList.objects.filter(**request.data)
            watchList.delete()
            response = {
                'status': True,
                'message': 'Film, listenizden kaldırıldı'
            }

            return Response(response, status=200)
        
        response = {
            'status': False,
            'message': "Bu film, listenizde mevcut değil"
        }

        return Response(response, status=400)

    def get(self, request):
        watchlist = WatchList.objects.filter(**request.data)
        serializer = WatchlistSerializer(watchlist, many=True)
        watchlist = serializer.data

        editedWatchlist = []
        for item in watchlist:
            movie = Movie.objects.filter(id=item['movie'])
            movieSerializer = MovieSerializer(movie, many=True)
            movie = movieSerializer.data
            editedWatchlist.append(movie[0])

        response = {
            'status': True,
            'message': 'İzleme listesi başarıyla getirildi',
            'data': {
                'watchlist': editedWatchlist
            }
        }

        return Response(response, status=200)