from django.urls import path
from .views import PredictTomato, TomatoList

urlpatterns = [
    path("tomato/predict/", PredictTomato.as_view(), name="tomato-predict"),
    path("tomato/predicted/<uuid:farmer_id>/", TomatoList.as_view(), name="tomato-predicted")
]
