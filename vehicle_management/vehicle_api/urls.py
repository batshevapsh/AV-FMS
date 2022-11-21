from vehicle_api.views import car
from django.urls import path


urlpatterns = [
   
    path('car/', car.view_all_cars),
]