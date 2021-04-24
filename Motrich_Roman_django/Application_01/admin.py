from django.contrib import admin

# Register your models here.

from .models import MyGoods

admin.site.register(MyGoods)