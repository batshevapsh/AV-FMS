from collections import namedtuple
from datetime import datetime, date

from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from core.models import Car,Task,User
from task.serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, get_object_or_404, ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from rest_framework import (
    viewsets,
   generics,
    status,
)


class CreateTaskView(CreateAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    serializer_class=TaskSerializer

    def perform_create(self, serializer):
        pk = self.request.data.get('pk')
        user_id=self.request.user.id
        #user=car.objects.get(id=pk) to do
        car = Car.objects.get(id=3)
        #user=User.objects.get(id=user_id) to do
        user=User.objects.get(id=2)
        task_active=Task.objects.filter(is_active=True)
        task_active_with_curent_car= task_active.filter(car=car)
        #task_active_with_curent_user=task_active.filter(user=user)
        if(task_active_with_curent_car):
           return Response("car not avlaibele", status=status.HTTP_400_BAD_REQUEST)
        #if (task_active_with_curent_user):
            #return Response("you have open task", status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=user, car=car,is_active=True)
        car.availability=False
        car.save() 

class ReleaseTaskView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_active=False
        task.end_date=datetime.datetime.now()
        car=Car.objects.get(pk=task.car.pk)
        task.save()
        car.save()
        return Response({'Release': True})

class GetTaskView(ReadOnlyModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
            vehicle_number=self.request.query_params.get('vehicle_number')
            return self.queryset\
            .filter(car__vehicle_number=vehicle_number)



        



        
        




