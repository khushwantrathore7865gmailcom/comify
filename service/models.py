from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Service(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    category = models.CharField(max_length=250,null=True)
    desc = models.CharField(max_length=250,null=True)
    whatsapp = models.CharField(max_length=12,null=True)
    instagram = models.CharField(max_length=250,null=True)
    phone = models.CharField(max_length=12,null=True)
    profile_pic = models.ImageField(upload_to='service_profile/', null=True)


class Feature_service(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    on_date = models.DateTimeField(auto_now_add=True)
    Subscription_plan = models.CharField(max_length=50)


class Baner(models.Model):
    Title = models.CharField(max_length=25)
    message = models.CharField(max_length=50)
    Baner_Display = models.BooleanField(default=False)
