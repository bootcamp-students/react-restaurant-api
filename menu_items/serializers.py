from rest_framework import serializers

from menu_items.models import Category, Item, Cuisine

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['label']


class ItemSerializer(serializers.ModelSerializer):
    cuisine = CuisineSerializer()
    category = CategorySerializer()

    class Meta:
        model = Item
        fields = ['id', 'category', 'cuisine', 'title', 'price', 'description', 'spicy_level']