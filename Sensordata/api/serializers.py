from rest_framework import serializers 
from ..models import Sensor
from Account.api.serializers import FarmerSerializer

class SensorSerializer(serializers.ModelSerializer):
   "This the serializer for the model : Sensor"
   farmer = FarmerSerializer()
   class Meta:
        model = Sensor
        fields = "__all__"

   

