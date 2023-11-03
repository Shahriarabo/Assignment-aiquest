from django.db import models

# Create your models here.
class customer_info(models.Model):
    customer_id = models.IntegerField()
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    price = models.IntegerField()
