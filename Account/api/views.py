from rest_framework.generics import(
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
)
from .serializers import (
    FarmerSerializer,
    ExpertSerializer,
    VerifySerializer,
)
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import(
    AllowAny,
    #IsAuthenticated,
    #IsAdminUser,
    #IsAuthenticatedOrReadOnly,
    #DjangoModelPermissions,
    #DjangoModelPermissionsOrAnonReadOnly,
    #DjangoObjectPermissions
)
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta
from rest_framework.response import Response
from ..models import (
    Farmer,
    Expert,
    Verify,
)


class FarmerCreate(CreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [AllowAny,]

class FarmerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [AllowAny, ]

class ExpertCreate(CreateAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    permission_classes = [AllowAny, ]

class ExpertRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    permission_classes = [AllowAny, ]

class TokenVerify(APIView):
    "this will regenerate the token or verify the token"
    
    def post(self, requests, format=None):
        farmer_id = requests.data.pop("farmer_id", None)
        expert_id = requests.data.pop("expert_id", None)
        
        if farmer_id and expert_id:
            msg = "Please select anyone of user"
            raise ValidationError(msg)
        if not farmer_id and not expert_id:
            msg = "Please select any one the user"
            raise ValidationError(msg)

        contact_no = requests.data.pop("contact_no", None)
        if not contact_no:
            msg = "Please Provide the conatct no of the User"
            raise ValidationError(msg)

        passed_token = requests.data.pop("token", None)
        if not passed_token:
            msg = "Please provide the token for verification"
            raise ValidationError(msg)
        current_time = timezone.now()

        if farmer_id and contact_no:
            verify  = Verify.objects.filter(
                farmer_account__farmer_id= farmer_id,
                contact_no=contact_no,
            ).order_by("create_stamp").first()

            if verify.create_stamp-current_time < timedelta(hours=1):
                if str(passed_token) == str(verify.token):
                    verify.verified = True
                    verify.save()
                else:
                    msg = "Please provide the correct token"
                    raise ValidationError(msg)
            return Response({"Result":"Your Account is varified"}, status= status.HTTP_202_ACCEPTED) 
        
        elif expert_id and contact_no:
            verify  = Verify.objects.filter(
                expert_account__expert_id= expert_id,
                contact_no=contact_no,
            ).order_by("create_stamp").first()
            if verify.create_stamp-current_time < timedelta(hours=1):
                if str(passed_token) == str(verify.token):
                    verify.verified = True
                    verify.save()
                else:
                    msg = "Please provide the correct token"
                    raise ValidationError(msg)
                return Response({"Result":"Your Account is varified"}, status= status.HTTP_202_ACCEPTED)
    

        """
        {
            farmer_id:
            expert_id:
            contact_no:
            token:
        }
        """

class TokenRegerate(APIView):
    def post(self, requests, format=None):
        farmer_id = requests.data.pop("farmer_id", None)
        expert_id = requests.data.pop("expert_id", None)
        
        if farmer_id and expert_id:
            msg = "Please select anyone of user"
            raise ValidationError(msg)
        if not farmer_id and not expert_id:
            msg = "Please select any one the user"
            raise ValidationError(msg)

        contact_no = requests.data.pop("contact_no", None)
        if not contact_no:
            msg = "Please Provide the conatct no of the User"
            raise ValidationError(msg)
        
        if farmer_id and contact_no:
            verify  = Verify.objects.filter(
                farmer_account__farmer_id= farmer_id,
                contact_no=contact_no,
            ).order_by("create_stamp").first()
            verify.change_requset = True
            verify.save()
            
        elif contact_no and expert_id:
            verify  = Verify.objects.filter(
                expert_account__expert_id= expert_id,
                contact_no=contact_no,
            ).order_by("create_stamp").first()
            verify.change_requset = True
            verify.save()
        

