from django.db import models

# Create your models here.
class Singup(models.Model):
    frist_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    comfrom_password = models.CharField(max_length=20)
    which_one_flowers = models.IntegerField()
    comment = models.CharField(max_length=50)
    Agree_to_terms_and_conditions = models.CharField(max_length=20)
    Do_you_want_to_buy_flowers_in_my_shop = models.CharField(max_length=20)
