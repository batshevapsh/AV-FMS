
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, data):
        user = User.objects.create(**data)
        user.set_password(data.get('password'))
        user.save()
        return user

    