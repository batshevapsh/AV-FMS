from core.models import Car,Task
from rest_framework import serializers

from user.serializers import UserSerializer



class TaskSerializer(serializers.ModelSerializer):
     class Meta:
        model = Task
        fields = '__all__'
        depth = 2