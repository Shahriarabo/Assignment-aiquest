from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import (
    Customer,
    Product,
    Card,
    OrderPlaced
)

# customer model

@admin.register(Customer)
class customerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'division', 'district', 'thana', 'villprroad', 'zipcode']
    
    
    
    
# Product model

@admin.register(Product)
class productadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price','descrition', 'brand', 'category', 'product_image']
    
    
    
# Card model

@admin.register(Card)
class cardadmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quntity']
    
    
    
# OrderPlaced model

@admin.register(OrderPlaced)
class orderplacedadmin(admin.ModelAdmin):
    list_display = ['id', 'user','customer', 'product', 'quantity', 'ordered_date', 'status']
