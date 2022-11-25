from core.models import Car,Task
from rest_framework import serializers

from user.serializers import UserSerializer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['vehicle_number','availability','manufacturer']
class TaskSerializer(serializers.ModelSerializer):
     class Meta:
        model = Task
        fields = '__all__'
        depth = 2