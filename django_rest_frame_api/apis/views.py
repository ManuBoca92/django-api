from django.shortcuts import render

from rest_framework import viewsets, serializers
from .models import City, Users
from .serializers import CitySerializer, UsersSerializer
from rest_framework.views import APIView, Response

# Create your views here.


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CustomView(APIView):
    def get(self, request, format=None):

        return Response("Some Get Response")
