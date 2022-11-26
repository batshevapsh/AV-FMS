"""vehicle_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path



""""
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


# Routers provide an easy way of automatically determining the URL conf.


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  #  path('api/vehicle/', include('vehicle_api.urls')),
    path('api/user/', include('user.urls')),
    path('api/car/', include('car.urls')),
      path('api/task/', include('task.urls')),
    #path('api/account/', include('car.urls'))
  
   
]