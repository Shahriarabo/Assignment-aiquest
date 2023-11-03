from django.contrib import admin
from . models import customer_info
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','customer_id','name','email','price')
admin.site.register(customer_info, CustomerAdmin)