from rest_framework import serializers
from FleaMarketItem.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user', 'name', 'description', 'condition', 'brand', 'price', 'category')
        model = Item


class EditItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description', 'condition', 'brand', 'price', 'category')