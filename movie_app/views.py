from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSer

@api_view(['GET'])
def test_api_view(request):
  dict={
    "text": "hello",
    "int": 100
  }
  return Response(data=dict, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_list_api_view(request):
  movie = Movie.objects.all()
  ser = MovieSer(movie, many=True)
  return Response(data=ser.data)
