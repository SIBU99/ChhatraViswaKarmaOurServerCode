from rest_framework.generics import(
    ListAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.parsers import (
    #JSONParser,
    FormParser,
    MultiPartParser,
    #FileUploadParser,
)
from Account.models import Farmer
from rest_framework.response import Response
from rest_framework import status
from Paddy.models import Paddy
from PlantDiseaseDetection.paddy_ml_data.h5TestPaddy import load
from .serializers import PaddySerializer

class PredictPaddy(APIView):
    parser_classes = (
        FormParser,
        MultiPartParser,
    )
    def post(self, request, format=None):
        "this will run ever the post is called"
        image = request.data.get("image",None)
        if not image:
            msg = "Plesae provide the Image"
            raise ValidationError(msg)
        data = list(load(image))[0]

        farmer_id = request.data.get("farmer_id" , None)
        if not farmer_id:
            msg = "Please provide the Farmer ID"
            raise ValidationError(msg)
        try:
            farmer = Farmer.objects.get(farmer_id = farmer_id)
        except:
            msg = "Please provide a valid Farmer ID"
            raise ValidationError(msg)
        try:
            """
            paddy = Paddy.objects.create(
                image = imag
                farmer = farmer,
                result_tag = True,
                disease1 = data[0],
                disease2 = data[1],
                disease3 = data[2],
            )
            """
            paddy  = Paddy()
            paddy.image = image
            paddy.farmer = farmer
            paddy.result_tag = True
            paddy.disease1 = data[0]
            paddy.disease2 = data[1]
            paddy.disease3 = data[2]
            paddy.save()
        except:
            msg = "System Error in data saving"
            raise ValidationError(msg)

        serializer = PaddySerializer(paddy)

        return Response(serializer.data, status = status.HTTP_201_CREATED)


class PaddyList(ListAPIView):
    #queryset = Corn.objects.all()
    serializer_class = PaddySerializer
    #permission_classes = []
    
    def get_queryset(self):
        
        farmer_id = self.kwargs['farmer_id']
        return Paddy.objects.filter(farmer__farmer_id=farmer_id)