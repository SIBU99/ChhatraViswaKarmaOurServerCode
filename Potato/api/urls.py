from django.urls import path
from .views import PredictPotato, PotatoList

urlpatterns = [
    path("potato/predict/", PredictPotato.as_view(), name="potato-predict"),
    path("potato/predicted/<slug:farmer_id>/",PotatoList.as_view(), name="potato-predicted"),
]

