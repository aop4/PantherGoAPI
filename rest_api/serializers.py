from rest_framework import serializers
from rest_api.models import *

basic_info = ('uuid', 'latitude', 'longitude', 'name', 'id')

class BasicAcademicBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicBuilding
        fields = basic_info

class BasicRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = basic_info

class BasicOutdoorAttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutdoorAttraction
        fields = basic_info

class BasicSportsFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsFacility
        fields = basic_info

class BasicMuseumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museum
        fields = basic_info


class DetailedAcademicBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicBuilding
        fields = '__all__'

class DetailedRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class DetailedOutdoorAttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutdoorAttraction
        fields = '__all__'

class DetailedSportsFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsFacility
        fields = '__all__'

class DetailedMuseumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museum
        fields = '__all__'

