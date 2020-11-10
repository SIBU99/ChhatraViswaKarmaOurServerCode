from django.db import models
import requests as req
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4
from random import choice
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError, ObjectDoesNotExist

def token_generate():
    "this will generate the token for the authentication"
    print("Token Generated")
    token = 0
    l = [ i for i in range(10) ]
    for _ in range(4):
        temp_token = choice(l)
        token *= 10
        token += temp_token
    else:
        return token

def send_the_otp(name, otp, phone_no):
    "this will send the otp using fast2sms api"
    url = "https://www.fast2sms.com/dev/bulk"
    #hide the api key
    key = "1zrRO4aB5F2spjYolkVqNtxAdJeZuHnhEDWMX9P3KS8UGIic7Q0Xo3yEaK1znpNJO8cdeSCGxFbMrALU"
    #key = os.environ.get("sms_api", None)
    querystring = dict()
    count = 3
    while count:
        querystring["authorization"] = key
        querystring["sender_id"]= "FSTSMS"
        querystring["language"]= "english"
        querystring["route"]="qt"
        querystring["numbers"] = f"{phone_no}"
        querystring["message"] = "20096"
        querystring["variables"] = "{BB}|{AA}"
        querystring["variables_values"] = f"{name}|{otp}"
    
        headers = {
        'cache-control': "no-cache"
        }
        count -= 1
        response = req.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            print("Send the otp")
            return 200
    else:
        print("Failed the otp")
        return 404

# Create your models here.
class Farmer(models.Model):
    "this will hold the information of the Framer<basic>"
    farmer_id = models.UUIDField(
        verbose_name="Farmer ID",
        help_text = "Do Not Edit",
        default=uuid4,
        primary_key=True,
        unique=True,
    )
    name = models.CharField(
        verbose_name="Full Name", 
        max_length=100,
    )
    contact_no = models.BigIntegerField(
        verbose_name="Contact No",
        help_text="Contact No OF the Framer"
    )
    verified = models.BooleanField(
        verbose_name="Verified Account",
        default = False
    )
    acc = models.OneToOneField(
        User,
        verbose_name="User",
        help_text = "User Information", 
        on_delete=models.CASCADE
    )
    when = models.DateTimeField(
        verbose_name = "When",
        auto_now_add=True,
        help_text = "When the account created",
    )

    @property
    def allow_period(self):
        "this will return the allow period of the account to use with out verification"
        if self.verified:
            return True
        else:
            if self.when - timezone.now() < timedelta(days=7):
                return True
            else:
                return False


    class Meta:
        verbose_name = "Farmer"
        verbose_name_plural = "Farmers"

    def __str__(self):
        return self.name

@receiver(post_save, sender=Farmer)
def Farmer_post_save_receiver(sender, instance, **kwargs):
    try:
        Verify.objects.get(farmer_account=instance)
    except Verify.DoesNotExist:
        verify = Verify()
        verify.farmer_account = instance
        verify.save()

class Expert(models.Model):
    "this will hold the information of  the expert<basic>"
    expert_id = models.UUIDField(
        verbose_name="Expert ID",
        help_text="Do not edit",
        default=uuid4,
        primary_key=True,
        unique=True,
    )
    name = models.CharField(
        verbose_name="Full Name", 
        max_length=100,
    )
    contact_no = models.BigIntegerField(
        verbose_name="Contact No",
        help_text="Contact No OF the Framer"
    )
    verified = models.BooleanField(
        verbose_name="Verified Account",
        default = False
    )
    acc = models.OneToOneField(
        User,
        verbose_name="User",
        help_text = "User Information", 
        on_delete=models.CASCADE
    )
    when = models.DateTimeField(
        verbose_name = "When",
        auto_now_add=True,
        help_text = "When the account created",
    )

    class Meta:
        verbose_name = "Expert"
        verbose_name_plural = "Experts"

    def __str__(self):
        return self.name

@receiver(post_save, sender=Expert)
def Expert_post_save_receiver(sender, instance, **kwargs):
    try:
        Verify.objects.get(expert_account=instance)
    except Verify.DoesNotExist:
        print("pass1")
        verify = Verify()
        verify.expert_account = instance
        print("pass2")
        verify.save()

class Verify(models.Model):
    "this will verify the user's contact no"
    farmer_account = models.ForeignKey(
        "Account.Farmer", 
        verbose_name="Farmer Account", 
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        related_name="tokenfarmer"
    )
    expert_account = models.ForeignKey(
        "Account.Expert", 
        verbose_name="Expert Account", 
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        related_name="tokenexpert"
    )
    contact_no = models.BigIntegerField(
        verbose_name="Contact Number",
        help_text = "Conatct Numeber of the user",
        blank=True
    )

    token = models.IntegerField(
        verbose_name="Token",
        help_text="Token for authentication <6 Digits>",
        blank=True
    )
    create_stamp = models.DateTimeField(
        verbose_name="When Created",
        blank=True
    )
    verified = models.BooleanField(
        verbose_name="Verified Token",
        default=False,
    )
    change_request = models.BooleanField(
        verbose_name="Change Request",
        default=True
    )

    @property
    def name(self):
        if self.farmer_account:
            return self.farmer_account.name
        elif self.expert_account:
            return self.expert_account.name
    
    def clean(self):
        if self.farmer_account and self.expert_account:
            raise ValidationError("Please select any one of the account")
        elif not self.farmer_account and not self.expert_account:
            raise ValidationError("Please select the option")
        

    def save(self, *args, **kwargs):
        "this will triger when it is save"
        if self.farmer_account:
            self.contact_no = self.farmer_account.contact_no
        elif self.expert_account:
            self.contact_no = self.expert_account.contact_no
        if self.change_request: #request for a otp to verify validity upto 1hr
            if self.create_stamp:
                check_time = timezone.now()
                if check_time - self.create_stamp < timedelta(hours=1):
                    self.token = token_generate()
                    self.create_stamp = timezone.now()
                    self.change_request = False
                    code = send_the_otp(name=self.name, otp= self.token, phone_no=self.contact_no)
                    if code is 400:
                        raise ValidationError("There is technical issue with otp generation")
                else:
                    raise ValidationError("Your Account Token is expired create a new one.")
            else:
                self.token = token_generate()
                self.create_stamp = timezone.now()
                self.change_request = False
                code = send_the_otp(name=self.name, otp= self.token, phone_no=self.contact_no)
                if code is 400:
                    raise ValidationError("There is technical issue with otp generation")
        elif self.verified: #check for verification if not verified contact the customer care support
            check_time = timezone.now()
            if check_time - self.create_stamp < timedelta(hours=1):
                self.verified = True
            else:
                self.verified = False 
        super(Verify, self).save()

@receiver(post_save, sender=Verify)
def verify_post_save_receiver(sender,instance, **kwargs):
    if instance.farmer_account:
        if instance.verified:
            farmer = Farmer.objects.get(farmer_id = instance.farmer_account.farmer_id)
            farmer.verified = True
            farmer.save()
    elif instance.expert_account:
        if instance.verified:
            expert = Expert.objects.get(expert_id = instance.expert_account.expert_id)
            expert.verified = True
            expert.save()


#arn:aws:sns:ap-south-1:592610022187:regional
"""
#! This will hold the information of fast2sms api integration
{
    "return":true,
    "data":[
        {
            "template_id":20096,
            "message":"Hello {#BB#}, Your otp for verification is {#AA#}, if you didn't request then ignore it."
        }
    ]
}
#?This all  the template for the task where there is only two data {#BB#}->For the user name
#?{#AA#}->For the User contact no
"""