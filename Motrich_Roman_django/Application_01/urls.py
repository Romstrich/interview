from django.contrib import admin
from django.urls import path
from .views import index, all_goods_show, GoodsListView,ajax_test_01

urlpatterns = [
    path('',index),
    path('ajax_test/',ajax_test_01),
    path('goods/',all_goods_show),
    path('goods_lclass/',GoodsListView.as_view())

]