from django.contrib import admin

# Register your models here.
from .models import Category, Item, Cuisine

admin.site.register(Cuisine)
admin.site.register(Category)
admin.site.register(Item)