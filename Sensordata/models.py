from django.db import models
from Account.models import Farmer

# Create your models here.
class Sensor(models.Model):
    temp = models.CharField(
        verbose_name="Temperature", 
        max_length=50,
    )
    potasium = models.CharField(
        verbose_name = "Potasium", 
        max_length=50,
    )
    moisture = models.CharField(
        verbose_name="Moisture",
        max_length=20,
    )
    humidity = models.CharField(
        verbose_name="Humidity",
        max_length=20,
    )
    nitrogen = models.CharField(
        verbose_name="Nitrogen",
        max_length=20
    )
    tds = models.CharField(
        verbose_name="TDS", 
        max_length=50
    )
    ph = models.CharField(
        verbose_name="P.H",
        max_length=50
    )
    turbidity = models.CharField(
        verbose_name="Turbidity", 
        max_length=50
    )
    phosphorus = models.CharField(
        verbose_name="Phosphorus", 
        max_length=50
    )
    farmer = models.ForeignKey(
        "Account.Farmer", 
        verbose_name="Farmer", 
        on_delete=models.CASCADE,
        related_name="FarmerSensorData",
    )