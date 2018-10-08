from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_api.models import *
from rest_api.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from drf_multiple_model.views import ObjectMultipleModelAPIView

class Register(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        email = request.data.get('email', None)
        if not (username and email and password):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                data={'message': 'Username, password, and email required'})
        if User.objects.filter(username=username):
            return Response(status=status.HTTP_409_CONFLICT, data={'message': 'Username exists'})
        user = User.objects.create_user(username, email, password)
        user.save()

class Login(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if not (username and password):
            return Response(status=status.HTTP_400_BAD_REQUEST, 
                data={'message': 'Username and password required'})
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        login(request, user) # ideally we should send an auth token

# return a categorized collection of all locations
class Locations(ObjectMultipleModelAPIView):
    # get() is implied
    querylist = [
        {
            'queryset': AcademicBuilding.objects.all(), 
            'serializer_class': BasicAcademicBuildingSerializer
        },
        {
            'queryset': Restaurant.objects.all(), 
            'serializer_class': BasicRestaurantSerializer
        },
        {
            'queryset': OutdoorAttraction.objects.all(), 
            'serializer_class': BasicOutdoorAttractionSerializer
        },
        {
            'queryset': SportsFacility.objects.all(), 
            'serializer_class': BasicSportsFacilitySerializer
        },
        {
            'queryset': Museum.objects.all(), 
            'serializer_class': BasicMuseumSerializer
        },
    ]

def retrieve_instance(model_class, id, serializer_class):
    # attempt to retrieve row from database's model_class table
    instance = model_class.objects.filter(id=id).first()
    # if we couldn't find it, send a 404
    if instance is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # if we could, serialize it and send it to the client
    serializer = serializer_class(instance)
    return Response(serializer.data)

class AcademicBuildingInstance(APIView):
    def get(self, request, id):
        return retrieve_instance(AcademicBuilding, id,
            DetailedAcademicBuildingSerializer)

class RestaurantInstance(APIView):
    def get(self, request, id):
        return retrieve_instance(Restaurant, id,
            DetailedRestaurantSerializer)

class OutdoorAttractionInstance(APIView):
    def get(self, request, id):
        return retrieve_instance(OutdoorAttraction, id,
            DetailedOutdoorAttractionSerializer)

class SportsFacilityInstance(APIView):
    def get(self, request, id):
        return retrieve_instance(SportsFacility, id,
            DetailedSportsFacilitySerializer)

class MuseumInstance(APIView):
    def get(self, request, id):
        return retrieve_instance(Museum, id,
            DetailedMuseumSerializer)

