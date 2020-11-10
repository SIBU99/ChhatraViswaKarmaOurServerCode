from django.urls import path
from .views import PredictPaddy, PaddyList

urlpatterns = [
    path("paddy/predict/", PredictPaddy.as_view(), name="paddy-predict"),
    path("paddy/predicted/<uuid:farmer_id>/", PaddyList.as_view(), name="paddy-predicted"),
]
