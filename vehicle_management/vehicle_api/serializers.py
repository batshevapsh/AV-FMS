from vehicle_api.models import Car
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['vehicle_number','availability','manufacturer']