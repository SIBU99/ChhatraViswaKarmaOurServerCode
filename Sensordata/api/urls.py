from django.urls import path

from .views import (
    SensorDataReciever, 
    SensorList
)


urlpatterns = [
  path("sensor/data/", SensorDataReciever.as_view(), name="Sensor-data"),
  path("sensor/data/get/", SensorList.as_view(), name="Sensor-list"),
]

