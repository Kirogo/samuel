from django.contrib import admin
from . models import Food, Restaurant, Item

# Register your models here.
admin.site.register(Food)
admin.site.register(Item)
admin.site.register(Restaurant)

