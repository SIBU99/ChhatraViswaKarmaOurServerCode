from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import SensorSerializer
from rest_framework.status import (
    HTTP_202_ACCEPTED
)
from Account.models import Farmer
from ..models import Sensor
from .serializers import SensorSerializer

class SensorDataReciever(APIView):
    "this will recive the post data of sensor"
    
    def post(self, request,format=None):
        "this will trigger when there will the post request"
        print(request.data)
        farmer_id = request.data.get("farmer_id", None)
        if not farmer_id:
            msg = "Farmer ID is not provided"
            raise ValidationError(msg)
        try:
            farmer = Farmer.objects.get(farmer_id = farmer_id)
        except:
            msg = "Please provide the Valid Farmer ID"
            raise ValidationError(msg)

        try:
            temp = request.data["temp"]
            potasium = request.data["potasium"]
            moisture = request.data["moisture"]
            humidity = request.data["humidity"]
            nitrogen = request.data["nitrogen"]
            tds = request.data["tds"] 
            ph = request.data["ph"]
            turbidity = request.data["turbidity"]
            phosphorus = request.data["phosphorus"]
        except:
            msg ="Please Provide The correct Data set"
            raise ValidationError(msg)
        try:
            sensor = Sensor.objects.create(
                temp = temp,
                potasium =potasium,
                moisture = moisture,
                humidity = humidity,
                nitrogen = nitrogen,
                tds = tds,
                ph = ph,
                turbidity = turbidity,
                phosphorus  = phosphorus,
                farmer = farmer              
            )
        except:
            msg = "System Error provided"
            raise ValidationError(msg)

        serializer = SensorSerializer(sensor)
        
        return Response(serializer.data, status = HTTP_202_ACCEPTED)

class SensorList(ListAPIView):
    "this will provide the list of the "
    serializer_class = SensorSerializer

    def get_queryset(self):
        sensor = Sensor.objects.all()
        farmer_id = self.request.query_params.get('farmer', None)
        if farmer_id:
            sensor = Sensor.objects.filter(farmer__farmer_id = farmer_id)
        return sensor

