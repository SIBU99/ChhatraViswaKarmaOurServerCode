from rest_framework import serializers
from ..models import Tomato
from Account.api.serializers import FarmerSerializer
from Account.models import Farmer
from rest_framework.exceptions import ValidationError

class TomatoSerializer(serializers.ModelSerializer):
    "This the serializer for the model : Corn"
    farmer = FarmerSerializer(read_only = True)
    class Meta:
        model = Tomato
        fields = [
            "id",
            "farmer",
            "image",
            "result_tag",
            "disease1",
            "disease2",
            "disease3",
            "disease4",
            "disease5",
            "disease6",
            "disease7",
            "disease8",
            "when",
            "map_disease",
        ]

    