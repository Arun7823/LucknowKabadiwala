from django.db import models
class Contact(models.Model):
    username=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    item=models.TextField()
# Create your models here.
