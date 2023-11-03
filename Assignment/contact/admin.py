from django.contrib import admin
from . models import Singup

# Register your models here.
class singupforms(admin.ModelAdmin):
    list_display = ('frist_name', 'last_name', 'email', 'password', 'comfrom_password', 'which_one_flowers', 'comment', 'Agree_to_terms_and_conditions', 'Do_you_want_to_buy_flowers_in_my_shop')
admin.site.register(Singup,singupforms)