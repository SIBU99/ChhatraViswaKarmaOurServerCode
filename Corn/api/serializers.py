from rest_framework import serializers
from ..models import Corn
from Account.api.serializers import FarmerSerializer
from Account.models import Farmer
from rest_framework.exceptions import ValidationError

class CornSerializer(serializers.ModelSerializer):
    "This the serializer for the model : Corn"
    farmer = FarmerSerializer(read_only = True)
    class Meta:
        model = Corn
        fields = [
            "id",
            "farmer",
            "image",
            "result_tag",
            "disease1",
            "disease2",
            "disease3",
            "when",
            "map_disease",
        ]

    
