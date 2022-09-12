from django.shortcuts import render
from rest_framework import viewsets

from menu_items.serializers import CategorySerializer, ItemSerializer, CuisineSerializer
from menu_items.models import Category, Item, Cuisine
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the menu index.")

def send_json(request):
    data = {}
    category = Category.objects.all().values()
    cuisine = Cuisine.objects.all().values()
    items = Item.objects.all().values()

    data['categories'] = list(category)
    data['cuisines'] = list(cuisine)
    data['menu_items'] = list(items)
    return JsonResponse(data)

class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
   queryset = Item.objects.all()
   serializer_class = ItemSerializer

class CuisineViewSet(viewsets.ModelViewSet):
   queryset = Cuisine.objects.all()
   serializer_class = CuisineSerializer