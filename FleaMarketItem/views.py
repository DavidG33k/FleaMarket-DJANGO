from django.shortcuts import render
from rest_framework import generics
from FleaMarketItem.models import Item
from FleaMarketItem.serializer import ItemSerializer
# Create your views here.


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
