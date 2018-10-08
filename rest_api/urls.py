"""rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('locations/', views.Locations.as_view()),
    url(r'^locations/Restaurants/(?P<id>[0-9]+)$', views.RestaurantInstance.as_view()),
    url(r'^locations/AcademicBuildings/(?P<id>[0-9]+)$', views.AcademicBuildingInstance.as_view()),
    url(r'^locations/OutdoorAttractions/(?P<id>[0-9]+)$', views.OutdoorAttractionInstance.as_view()),
    url(r'^locations/SportsFacilities/(?P<id>[0-9]+)$', views.SportsFacilityInstance.as_view()),
    url(r'^locations/Museums/(?P<id>[0-9]+)$', views.MuseumInstance.as_view()),
]
