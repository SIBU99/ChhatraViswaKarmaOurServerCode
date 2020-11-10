from django.db import models
   
# Create your models here.
def upload_potato(instance, filename):
    "this will return the path of the file where it will store"
    return f"potato/{instance.farmer.farmer_id}/{filename}"

class Potato(models.Model):
    "This is the model which will hold the information of uploaded corn images"
    image = models.ImageField(
        verbose_name="Image Uploaded",
        upload_to=upload_potato,
        height_field=None,
        width_field=None,
        max_length=None
    )
    farmer = models.ForeignKey(
        "Account.Farmer", 
        verbose_name="Farmer", 
        on_delete=models.CASCADE,
        related_name = "FarmerUploadsPotato"
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
        #dic["Northern Leaf Blight"] = self.disease3
        return dic

    def save(self, *args, **kwargs):
        super(Potato, self).save(*args, **kwargs)
    

    class Meta:
        verbose_name = "Potato"
        verbose_name_plural = "Potatoes"

    def __str__(self):
        return f"{self.when}"
    



