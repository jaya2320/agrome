from django.db import models

# Create your models here.

class Buyer(models.Model):
    
    description=models.TextField()
    address=models.CharField(max_length=30)
    name=models.CharField(max_length=15)
    city=models.CharField(max_length=15)
    state=models.CharField(max_length=15)
    code=models.IntegerField()
    phone1=models.BigIntegerField()
    phone2=models.BigIntegerField()
    phone_number=models.BigIntegerField()
    fees = models.IntegerField()
    profile_img=models.ImageField(upload_to="media1")

class Seller(models.Model):
    
    description=models.TextField()
    address=models.CharField(max_length=30)
    name=models.CharField(max_length=15)
    city=models.CharField(max_length=15)
    state=models.CharField(max_length=15)
    code=models.IntegerField()
    phone1=models.BigIntegerField()
    phone2=models.BigIntegerField()
    phone_number=models.BigIntegerField()
    fees = models.IntegerField()
    profile_img=models.ImageField(upload_to="media1")