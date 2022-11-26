from car import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import (
    path,
    include,
)

router = DefaultRouter()

app_name = 'car'
router.register('list', views.GetCarView)

urlpatterns = [
    path('', include(router.urls)),
    path('create', views.CreateCarView.as_view(), name=""),
    #path('', views.GetCarView.as_view(), name=""),
   
]