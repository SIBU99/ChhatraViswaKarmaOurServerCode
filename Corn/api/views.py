from rest_framework.generics import(
    ListAPIView,
    RetrieveDestroyAPIView,
)
#import django_filters.rest_framework
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
from Corn.models import Corn
from PlantDiseaseDetection.corn_ml_data.h5TestCorn import load
from .serializers import CornSerializer

class PredictCorn(APIView):
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
        data = load(image)
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
            corn = Corn.objects.create(
                image = image,
                farmer = farmer,
                result_tag = True,
                disease1 = data[0],
                disease2 = data[1],
                disease3 = data[2],
            )
        except:
            msg = "System Error in data saving"
            raise ValidationError(msg)

        serializer = CornSerializer(corn)

        return Response(serializer.data, status = status.HTTP_201_CREATED)

class CornList(ListAPIView):
    #queryset = Corn.objects.all()
    serializer_class = CornSerializer
    #permission_classes = []
    
    def get_queryset(self):
        
        farmer_id = self.kwargs['farmer_id']
        return Corn.objects.filter(farmer__farmer_id=farmer_id)


