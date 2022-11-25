from collections import namedtuple
from datetime import datetime, date

from django.http import JsonResponse
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from core.models import Car
from vehicle_api.serializers import CarSerializer
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def view_all_cars(request):
    """
    API endpoint for displaying all car details.
    """
    if request.method == 'GET':
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)