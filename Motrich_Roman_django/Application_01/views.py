from django.shortcuts import render
from django.http import HttpResponse,request
from .models import MyGoods
from django.views.generic import ListView
# Create your views here.
def index(request):
    return HttpResponse(f'Hellow, <b>{request.user.username}</b>')

def all_goods_show(request):
    all_goods=MyGoods.objects.all()
    good_str=', '.join(str(good) for good in all_goods)
    context={'page_header':'Все наши товары',
             'goods':all_goods}
    return render(request,template_name='goods_show.html',context=context)

class GoodsListView(ListView):
    template_name = 'goods_show.html'
    model = MyGoods
    context_object_name = 'goods'
