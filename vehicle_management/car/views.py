from collections import namedtuple
from datetime import datetime, date

from django.http import JsonResponse
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from core.models import Car,Task,User
from car.serializers import CarSerializer
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet

from rest_framework.generics import CreateAPIView, get_object_or_404, ListAPIView
from rest_framework import (
    viewsets,
   generics,
    status,
)
class CreateCarView(CreateAPIView):
    """Create a new car in the system."""
    serializer_class = CarSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAdminUser]



class GetCarView(viewsets.ModelViewSet):
    """View for gett List Car APIs."""
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get_queryset(self):
        if 'vehicle_number' in self.request.query_params:
            vehicle_number = self.request.query_params.get('vehicle_number')
            return self.queryset.filter(vehicle_number=vehicle_number)
        elif 'availability' in self.request.query_params:
            availabilityr = self.request.query_params.get('availabilityr')
            return self.queryset.filter(availabilityr=availabilityr)
        elif 'manufacturer' in self.request.query_params:
            manufacturer = self.request.query_params.get('manufacturer')
            return self.queryset.filter(manufacturer=manufacturer)
        return self.queryset




