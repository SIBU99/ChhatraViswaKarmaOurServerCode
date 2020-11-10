from rest_framework import serializers
from ..models import Potato
from Account.api.serializers import FarmerSerializer
from Account.models import Farmer
from rest_framework.exceptions import ValidationError

class PotatoSerializer(serializers.ModelSerializer):
    "This the serializer for the model : Corn"
    farmer = FarmerSerializer(read_only = True)
    class Meta:
        model = Potato
        fields = [
            "id",
            "farmer",
            "image",
            "result_tag",
            "disease1",
            "disease2",
            "when",
            "map_disease",
        ]

    