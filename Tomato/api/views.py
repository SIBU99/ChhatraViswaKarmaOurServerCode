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
from ..models import Tomato
from PlantDiseaseDetection.tomato_ml_data.Tomatoh5 import load
from .serializers import TomatoSerializer

class PredictTomato(APIView):
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
        data = list(load(image))
        data = list(map(float,data))
        farmer_id = request.data.get("farmer_id" , None)
        if not farmer_id:
            msg = "Please provide the Farmer ID"
            raise ValidationError(msg)
        try:
            farmer = Farmer.objects.get(farmer_id = farmer_id)
        except:
            msg = "Please provide a valid Farmer ID"
            raise ValidationError(msg)
        
        #try:
        tomato = Tomato.objects.create(
                image = image,
                farmer = farmer,
                result_tag = True,
                disease1 = data[0],
                disease2 = data[1],
                disease3 = data[2],
                disease4 = data[3],
                disease5 = data[4],
                disease6 = data[5],
                disease7 = data[6],
                disease8 = data[7],
        )

        """potato  = Potato()
            potato.image = image
            potato.farmer = farmer
            potato.result_tag = True
            potato.disease1 = data[0] 
            potato.disease2 = data[1]
            potato.save()"""
        #except:
        #    msg = "System Error in data saving"
        #    raise ValidationError(msg)

        serializer = TomatoSerializer(tomato)
    
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class TomatoList(ListAPIView):
    #queryset = Corn.objects.all()
    serializer_class = TomatoSerializer
    #permission_classes = []
    
    def get_queryset(self):
        
        farmer_id = self.kwargs['farmer_id']
        return Tomato.objects.filter(farmer__farmer_id=farmer_id)
