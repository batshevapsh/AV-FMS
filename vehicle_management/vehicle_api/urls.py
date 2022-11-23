from vehicle_api.views import car
from django.urls import path


urlpatterns = [
   
    path('', car.view_all_cars),
]