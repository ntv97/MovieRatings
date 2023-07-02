from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status

from .producer import publish
from .serializers import MovieSerializer, MovieInfoSerializer
from .models import Movie, MovieInfo
import random
import requests

# Create your views here.

class MovieViewSet(viewsets.ViewSet):
    def list(self, request):
        movies = Movie.objects
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        param = serializer.data['id']
        url = 'http://localhost:8000/api/movieinfo'
        new_url = "{}/{}".format(url, param)
        myobj = {'identifier': param, 'totalratings': serializer.data['ratings'], 'totalusers': 1}
        r = requests.post(new_url, json = myobj)
        publish('movie_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        movie = Movie.objects.get(id=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def update(self, request, pk=None):
        movie = Movie.objects.get(id=pk)
        serializer = MovieSerializer(instance=movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('movie_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def addrating(self, request, pk=None):
        movie = Movie.objects.get(id=pk)
        movieserial = MovieSerializer(movie)
        myobj = {'identifier': movieserial.data['id'], 'totalratings': request.data['ratings']}
        url = 'http://localhost:8000/api/movieinfo'
        new_url = "{}/{}".format(url, pk)
        r = requests.put(new_url, myobj)
        publish('rating_added', movieserial.data)
        return r

    def remove(self, request, pk=None):
        movie = Movie.objects.get(id=pk)
        movie.delete()
        publish('movie_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieInfoViewSet(viewsets.ViewSet):
    def list(self, request):
        movies = MovieInfo.objects
        serializer = MovieInfoSerializer(movies, many=True)
        return Response(serializer.data)
    def create(self, request, pk=None):
        serializer = MovieInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print('movie_info_created')
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def get(self, request, pk=None):
        movieinfo = MovieInfo.objects.get(identifier=pk)
        serializer = MovieInfoSerializer(movieinfo)
        return Response(serializer.data)
    def update(self, request, pk=None):
        movieinfo = MovieInfo.objects.get(identifier=pk)
        movieserial = MovieInfoSerializer(movieinfo)
        newtotratings = movieserial.data['totalratings'] + float(request.data['totalratings'])
        newusers = movieserial.data['totalusers'] + 1
        myobj = {'identifier': pk, 'totalratings': newtotratings, 'totalusers': newusers}
        url = 'http://localhost:8000/api/movieinfo'
        new_url = "{}/{}".format(url, pk)
        r = requests.delete(new_url)
        serializer = MovieInfoSerializer(instance=movieinfo, data=myobj)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        print("movie_info_updated")
    def remove(self, request, pk=None):
        movieinfo = MovieInfo.objects.get(identifier=pk)
        movieinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
