from django.db import models
from PlantDiseaseDetection.corn_ml_data.h5TestCorn import load
   
# Create your models here.
def upload_corn(instance, filename):
    "this will return the path of the file where it will store"
    return f"corn/{instance.id}/{filename}"

class Corn(models.Model):
    "This is the model which will hold the information of uploaded corn images"
    image = models.ImageField(
        verbose_name="Image Uploaded",
        upload_to=upload_corn,
        height_field=None,
        width_field=None,
        max_length=None
    )
    farmer = models.ForeignKey(
        "Account.Farmer", 
        verbose_name="Farmer", 
        on_delete=models.CASCADE,
        related_name = "FarmerUploadsCorn"
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
        verbose_name = "Nothern Leaf Blight",
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
        dic["Northern Leaf Blight"] = self.disease3
        return dic

    def save(self, *args, **kwargs):
        super(Corn, self).save(*args, **kwargs)
    

    class Meta:
        verbose_name = "Corn"
        verbose_name_plural = "Corns"

    def __str__(self):
        return f"{self.when}"
    


# @receiver(pre_save, sender=Corn)
# def corn_post_save_receiver(sender, instance,**kwargs):
#     img = instance.image.url
#     predict = load(img)
#     print("$"*30)
#     print(predict)


# @receiver(post_save, sender=Corn)
# def corn_post_save_receiver(sender, instance, **kwargs):
#     if not instance.result_tag:
#         img = instance.image.url
#         predict = load(img)
#         corn =Corn.objects.get(id = instance.id)
#         corn.result_tag = True
#         corn.disease1 = predict["Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot"]
#         corn.disease2 = predict["Corn_(maize)___Common_rust_"]
#         corn.disease3 = predict["Corn_(maize)___Northern_Leaf_Blight"]
#         corn.healthy = predict["Corn_(maize)___healthy"]
#         corn.save()
