from distutils.command.upload import upload
from email.policy import default
from enum import unique
from pickle import TRUE
from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
class Product(models.Model):
    
    product_name=models.CharField(max_length=50)
    product_price=models.CharField(max_length=50)
    product_img=models.FileField(upload_to="product/",max_length=250,null=True,default=None)
    
    #product_des=HTMLField
    #product_slug=AutoSlugField(populate_from='product_name',unique=True, null=True,default=None )


# Create your models here.
