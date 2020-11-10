from django.urls import path
from .views import (
    FarmerCreate, 
    FarmerRetrieveUpdateDestroyView, 
    ExpertCreate, 
    ExpertRetrieveUpdateDestroyView,
    TokenRegerate,
    TokenVerify,
)

urlpatterns = [
    path("farmers/", FarmerCreate.as_view(), name="Farmer-create"),
    path("farmers/<uuid:pk>/", FarmerRetrieveUpdateDestroyView.as_view(), name="Farmer-retrive"),
    path("expert/", ExpertCreate.as_view(), name="Expert-create"),
    path("expert/<uuid:pk>/", ExpertRetrieveUpdateDestroyView.as_view(), name="Expert-retive"),
    path("token/regenerate/", TokenRegerate.as_view(), name="token-regenerate"),
    path("token/verify/", TokenVerify.as_view(), name="token-verify"),
]