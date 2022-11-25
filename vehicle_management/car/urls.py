from car import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import (
    path,
    include,
)

router = DefaultRouter()

app_name = 'car'
#router.register('car', views.GetCarView)

urlpatterns = [
    path('', include(router.urls)),
    path('create', views.CreateCarView.as_view(), name=""),
    path('', views.CreateAPIView.as_view(), name=""),
    path('create-task/<int:pk>/<int:user_id>',views.CreateTaskView.as_view(), name='create-task'),
]