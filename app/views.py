from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def index(request):
    warehouses = Warehouse.objects.all()
    orders = Order.objects.filter(tracking="Pending")
    context = {
        "warehouse": warehouses,
        "orders": orders
    }

    return render(request, 'app/index.html', context=context)


def process_order(request, pk):
    if request.GET.get('get'):
        house = request.GET.get('house')
        warehouse = Warehouse.objects.get(pk=house)
        # item = Item.objects.get(request)
        # print(pk)
        # print(item.pick_up_from())
        # print(item.warehouse.all())
        # if house not in item.warehouse.values('pk'):
        #     item.warehouse.add(warehouse)
        #     item.save()

    order = get_object_or_404(Order, pk=pk)

    order_dict = {}

    for item in order.items.all():
        order_dict[item.product.sku] = Warehouse.objects.filter(products__sku=item.product.sku)

    context = {
        "order": order,
        "order_dict": order_dict
    }

    return render(request, 'app/order.html', context)
