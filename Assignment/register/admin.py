from django.contrib import admin
from . models import Teacher, Coustomer, Service
# Register your models here.

# ono to one relation=ship
@admin.register(Teacher)
class teacheradmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'teacher_reg', 'user']
    
    
# many to one relation=ship
@admin.register(Coustomer)
class coustomeradmin(admin.ModelAdmin):
    list_display = ['coustomer_id', 'coustomer_name','coustomer_address', 'user']
    
    
# many to many relationship
@admin.register(Service)
class servicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'item', 'service_man']
