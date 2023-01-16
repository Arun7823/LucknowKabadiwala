from django.db import models
class homeProduct(models.Model):
    
    product_name=models.CharField(max_length=50)
    product_price=models.CharField(max_length=50)
    product_img=models.FileField(upload_to="product/",max_length=250,null=True,default=None)


# Create your models here.
