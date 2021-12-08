from django.urls import path

from FleaMarketItem.views import *

urlpatterns = [
    # user
    path('item/', UserShowItemList.as_view()),
    path('item/add/', UserAddItemList.as_view()),
    path('item/edit/<int:pk>/', UserEditItemList.as_view()),

    #moderator
    path('users/', ModeratorShowUserList.as_view()),
    #path('item/moderator/(?P<user>\\d+)/', ModeratorShowItemList.as_view()),
    path('item-moderator/', ModeratorShowItemList.as_view()),
    path('item-moderator/edit/<int:pk>/', ModeratorEditItemList.as_view()),
]

