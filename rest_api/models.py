from django.db import models
from django.conf import settings
from shortuuidfield import ShortUUIDField

class Location(models.Model):
	# an abstract class--just used to avoid repetition of fields in children
	class Meta:
		abstract = True
	uuid = ShortUUIDField(editable=False) # unique identifier for location
	latitude = models.FloatField()
	longitude = models.FloatField()
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=10000)
	address = models.CharField(max_length=300)
	def __str__(self):
		return self.name	

class AcademicBuilding(Location):
	hoursOperation = models.TextField(max_length=500)

class Restaurant(Location):
	hoursOperation = models.TextField(max_length=500)
	menu = models.CharField(max_length=300)

class OutdoorAttraction(Location):
	types = (
		('Park', 'Park'),
		('Trail', 'Trail'),
		('Monument', 'Monument'),
		('Garden', 'Garden'),
		('Natural Wonder', 'Natural Wonder'),
		('Public Art', 'Public Art'),
		('Spooky Spot', 'Spooky Spot'),
	)
	type = models.CharField(choices=types, max_length=50)

class SportsFacility(Location):
	sports = models.CharField(max_length=150)
	teams = models.CharField(max_length=100)
	# assuming this is a link for now
	schedule = models.CharField(max_length=100)

class Museum(Location):
	hours = models.TextField(max_length=500)
	prices = (
		('$', '$'),
		('$$', '$$'),
		('$$$', '$$$'),
	)
	price = models.CharField(choices=prices, max_length=5)

