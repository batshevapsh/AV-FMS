from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from .models import UserProfile
from .serializers import UserSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response()


class CreateUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.save()
       
