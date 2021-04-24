from django.contrib import admin
from django.urls import path
from .views import index, all_goods_show, GoodsListView

urlpatterns = [
    path('',index),
    path('goods/',all_goods_show),
    path('goods_lclass/',GoodsListView.as_view())

]