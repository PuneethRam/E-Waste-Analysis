from django.db import models

# Create your models here.

class Resource(models.Model):
    username = models.CharField(max_length=100)
    device_type = models.CharField(null=True, blank=True,max_length=100)
    device_model = models.CharField(max_length=100)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.ImageField(upload_to='resource_pictures/')
    result=models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Recycle(models.Model):
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    device_type = models.CharField(null=True, blank=True,max_length=100)
    device_model = models.CharField(max_length=100)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.ImageField(upload_to='recycle_pictures/')
    pickup_type = models.CharField(max_length=50)
    pickup_date = models.DateTimeField(null=True, blank=True)
    stage=models.IntegerField(null=True,blank=True)
    requestid = models.CharField(null=True,blank=True,max_length=100)
    delivery_partner=models.CharField(null=True,blank=True,max_length=100)
    delivery_partner_phone=models.IntegerField(null=True,blank=True)
    claim_credit=models.IntegerField(null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class EwasteLocation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def _str_(self):
        return self.name    
    

class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100) 
    info  = models.CharField(max_length = 100, default = '')
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
