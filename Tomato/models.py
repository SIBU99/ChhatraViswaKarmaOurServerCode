from django.db import models
   
# Create your models here.
def upload_tomato(instance, filename):
    "this will return the path of the file where it will store"
    return f"tomato/{instance.farmer.farmer_id}/{filename}"

class Tomato(models.Model):
    "This is the model which will hold the information of uploaded corn images"
    image = models.ImageField(
        verbose_name="Image Uploaded",
        upload_to=upload_tomato,
        height_field=None,
        width_field=None,
        max_length=None
    )
    farmer = models.ForeignKey(
        "Account.Farmer", 
        verbose_name="Farmer", 
        on_delete=models.CASCADE,
        related_name = "FarmerUploadstomato"
    )
    result_tag = models.BooleanField(
        verbose_name="Proceed",
        default=False,
        editable=False
    )

    disease1 = models.FloatField(
        verbose_name = "Gray Leaf Spot",
        blank=True,
        default=0.0
    )
    disease2 = models.FloatField(
        verbose_name = "Common Rust",
        blank=True,
        default=0.0
    )
    disease3 = models.FloatField(
        verbose_name = "Common Rust",
        blank=True,
        default=0.0
    )
    disease3 = models.FloatField(
        verbose_name = "Common Rust",
        blank=True,
        default=0.0
    )
    disease4 = models.FloatField(
        verbose_name = "Common Rust",
        blank=True,
        default=0.0
    )
    disease5 = models.FloatField(
        verbose_name = "Common Rust",
        blank=True,
        default=0.0
    )
    disease6 = models.FloatField(
        verbose_name = "Common Rust",
        blank=True,
        default=0.0
    )
    disease7 = models.FloatField(
        verbose_name = "Common Rust",
        blank=True,
        default=0.0
    )
    disease8 = models.FloatField(
        verbose_name = "Common Rust",
        blank=True,
        default=0.0
    )

    when = models.DateTimeField(
        verbose_name = "Added On",
        help_text="When the image is  uploaded",
        auto_now_add=True,
    )

    @property
    def map_disease(self):
        dic = dict()
        dic["Gray Leaf Spot"] = self.disease1
        dic["Common Rust"] = self.disease2
        dic["Gray Leaf Spot"] = self.disease3
        dic["Common Rust"] = self.disease4
        dic["Gray Leaf Spot"] = self.disease5
        dic["Common Rust"] = self.disease6
        dic["Gray Leaf Spot"] = self.disease7
        dic["Common Rust"] = self.disease8
        #dic["Northern Leaf Blight"] = self.disease3
        return dic

    def save(self, *args, **kwargs):
        super(Tomato, self).save(*args, **kwargs)
    

    class Meta:
        verbose_name = "Tomato"
        verbose_name_plural = "Tomatoes"

    def __str__(self):
        return f"{self.when}"