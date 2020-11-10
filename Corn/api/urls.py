from django.urls import path
from .views import PredictCorn, CornList

urlpatterns = [
    path("corn/predict/", PredictCorn.as_view(), name="corn-predict"),
    path("corn/predicted/<slug:farmer_id>/",CornList.as_view(), name="corn-predicted"),
]
