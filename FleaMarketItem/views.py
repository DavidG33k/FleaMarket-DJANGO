from django.shortcuts import render
from rest_framework import generics
from FleaMarketItem.models import Item
from FleaMarketItem.permissions import IsUser, IsModerator
from FleaMarketItem.serializer import *
from rest_framework.exceptions import APIException
from django.contrib.auth import get_user_model


# user
class UserShowItemList(generics.ListAPIView):
    permission_classes = [IsUser]
    queryset = Item.objects.all()
    serializer_class = UserItemListSerializer

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class UserAddItemList(generics.CreateAPIView):
    permission_classes = [IsUser]
    serializer_class = UserItemListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserEditItemList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUser]
    queryset = Item.objects.all()
    serializer_class = UserEditItemSerializer


# MODERATOR
class ModeratorShowUserList(generics.ListAPIView):
    permission_classes = [IsModerator]
    serializer_class = ModeratorUserListSerializer

    def get_queryset(self):
        return get_user_model().objects.filter(is_superuser=False).exclude(groups__name='moderator')


class ModeratorEditItemList(generics.RetrieveDestroyAPIView):
    permission_classes = [IsModerator]
    queryset = Item.objects.all()
    serializer_class = ModeratorItemListSerializer


class ModeratorShowItemList(generics.ListAPIView):
    permission_classes = [IsModerator]
    queryset = Item.objects.all()
    serializer_class = ModeratorItemListSerializer

'''
class ModeratorShowItemListForUser(generics.ListAPIView):
    permission_classes = [IsModerator]
    serializer_class = ModeratorItemListSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        return Item.objects.filter(user=user)
'''