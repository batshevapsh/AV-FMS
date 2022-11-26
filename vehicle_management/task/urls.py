from task import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import (
    path,
    include,
)

router = DefaultRouter()

app_name = 'task'
router.register('list', views.GetTaskView)

urlpatterns = [
    path('', include(router.urls)),
    path('release-task/<int:pk>/<int:user_id>',views.ReleaseTaskView.as_view(), name='release-task'),
    
    path('create-task/<int:pk>/<int:user_id>',views.CreateTaskView.as_view(), name='create-task'),
]