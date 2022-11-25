from collections import namedtuple
from datetime import datetime, date

from django.http import JsonResponse
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from core.models import Car,Task,User
from car.serializers import CarSerializer,TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, get_object_or_404, ListAPIView
from rest_framework import (
    viewsets,
   generics,
    status,
)
class CreateCarView(CreateAPIView):
    """Create a new car in the system."""
    serializer_class = CarSerializer

class GetCarView(ListAPIView):
    """View for gett List Car APIs."""
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CreateTaskView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    serializer_class=TaskSerializer

    def perform_create(self, serializer):
        pk = self.request #.data.get('pk')
        user_id=self.request.data.get('user_id')
        print(pk,user_id)
        car = Car.objects.get(id=1)
        """user=self.request.user nead to bee"""
        user=User.objects.get(id=1)
        taskActiveWithCurentCar= Task.objects.filter(is_active=True,car=car)
        print(taskActiveWithCurentCar)
        taskActiveWithCurentUser=Task.objects.filter(is_active=True,user=user)
        print(taskActiveWithCurentUser)
        if(taskActiveWithCurentCar):
           return Response("car not avlaibele", status=status.HTTP_400_BAD_REQUEST)
        if (taskActiveWithCurentUser):
                return Response("you have open task", status=status.HTTP_400_BAD_REQUEST)
           #serializer.save(user=self.request.user, car=car) nead to be
        serializer.save(user=user, car=car)
        return Response(status=status.HTTP_201_CREATED)
        
        


