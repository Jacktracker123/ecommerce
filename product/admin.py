from django.contrib import admin
from . models import *
# Register your models here.
class Phone_display(admin.ModelAdmin):
    list_display=['name','image','price']
admin.site.register(Phone,Phone_display)

class Computer_display(admin.ModelAdmin):
    list_display=['name','image','price']
admin.site.register(Computer,Computer_display)