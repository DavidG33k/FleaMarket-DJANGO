from django.urls import path

from FleaMarketItem.views import ItemList, ItemDetail

urlpatterns = [
    path('',ItemList.as_view()),
    path('<int:pk>/', ItemDetail.as_view()),

]

