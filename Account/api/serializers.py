from rest_framework import serializers 
from ..models import (
    Farmer,
    Expert,
    Verify
)
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

class UserSerializer(serializers.ModelSerializer):
    "This the serializer for the model : User"
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
        ]
        extra_kwargs = {
            "password":{
                "write_only":True
            }
        }

class FarmerSerializer(serializers.ModelSerializer):
    "This the serializer for the model : Farmer"
    acc = UserSerializer()
    class Meta:
        model = Farmer
        fields = "__all__"
        read_only_fields = [
            "when",
            "farmer_id",
            "verified",
            "allow_period",
        ]
    
    def create(self, validated_data):
        "This will create the instance for many to many field " 
        acc  = validated_data.pop("acc", None)
        if not acc:
            msg = "PLease provide the information of the Farmer"
            raise ValidationError(msg)
        username= acc.pop("username", None)
        if not username:
            msg = "Please provide the username of the user"
            raise ValidationError(msg)
        password = acc.pop("password", None)
        if not password:
            msg = "Please provide the password of the password"
            raise ValidationError(msg)
        user = User.objects.create(
            username=username
        )
        user.set_password(password)
        user.save()
        
        farmer = Farmer.objects.create(**validated_data, acc=user)
        return farmer
    
    def update(self, instance, validated_data):
        "This is the update or put haeader for the file"
        instance.name = validated_data.pop("name", instance.name)
        instance.contact_no = validated_data.pop("contact_no", instance.contact_no)
        user_data = validated_data.pop("acc", None)
        if user_data:
            acc = instance.acc
            acc.username = user_data.get("username", acc.username)
            password = user_data.get("password", None)
            if password:
                acc.set_password(password)
            acc.save()

        return instance

class ExpertSerializer(serializers.ModelSerializer):
    "This the serializer for the model : Expert"
    acc = UserSerializer()
    class Meta:
        model = Expert
        fields = "__all__"
        read_only_fields = [
            "expert_id",
            "verified",
            "when",
            "allow_period",
        ]
    def create(self, validated_data):
        "This will create the instance for many to many field " 
        acc  = validated_data.pop("acc", None)
        if not acc:
            msg = "PLease provide the information of the Expert"
            raise ValidationError(msg)
        username= acc.pop("username", None)
        if not username:
            msg = "Please provide the username of the user"
            raise ValidationError(msg)
        password = acc.pop("password", None)
        if not password:
            msg = "Please provide the password of the password"
            raise ValidationError(msg)
        user = User.objects.create(
            username=username
        )
        user.set_password(password)
        user.save()
        
        expert =  Expert.objects.create(**validated_data, acc=user)
        return expert
    
    def upadate(self, instance, validated_data):
        "This is the update or put haeader for the file"
        instance.name = validated_data.pop("name", instance.name)
        instance.contact_no = validated_data.pop("contact_no", instance.contact_no)
        user_data = validated_data.pop("acc", None)
        if user:
            user = instance.acc
            user.username = user_data.get("username", user.username)
            password = user_data.get("password", user.password)
            if password:
                user.set_password(password)
            user.save()            

        return instance

class VerifySerializer(serializers.ModelSerializer):
    "This the serializer for the model : Verify"
    farmer_account = FarmerSerializer()
    expert_account = ExpertSerializer()
    class Meta:
        model = Verify
        fields = [
            "id",
            "farmer_account",
            "expert_account",
            "token",
            "create_stamp",
            "verified",
            "change_request"
        ]
        read_only_fields = [
            "id",
            "token",
            "create_stamp",
            ]
    
    def create(self, validated_data):
        "This will create the instance for many to many field " 
        farmer_account = validated_data.pop("farmer_account", None)
        expert_account = validated_data.pop("expert_account", None)
        if farmer_account:
            verify = Verify()
            verify.farmer_account = farmer_account
            verify.save()
        elif expert_account:
            verify = Verify()
            verify.expert_account = expert_account
            verify.save()
        return verify
    
    def upadate(self, instance, validated_data):
        "This is the update or put haeader for the file"
        if instance.farmer_account:
            instance.farmer_account = validated_data.pop("farmer_account", instance.farmer_account)
            instance.verified = validated_data.pop("verified", instance.verified)
            instance.change_request = validated_data.pop("change_request", instance.change_request)
        elif instance.expert_account:
            instance.expert_account = validated_data.pop("expert_account", instance.expert_account)
            instance.verified = validated_data.pop("verified", instance.verified)
            instance.change_request = validated_data.pop("change_request", instance.change_request)
        return instance