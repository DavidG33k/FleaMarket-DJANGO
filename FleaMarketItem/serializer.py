from rest_framework import serializers
from django.contrib.auth import get_user_model
from FleaMarketItem.models import Item


# user
class UserItemListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description', 'condition', 'brand', 'price', 'category')
        model = Item


class UserEditItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description', 'condition', 'brand', 'price', 'category')
        model = Item


# moderator
class ModeratorUserListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = get_user_model()


class ModeratorItemListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Item
