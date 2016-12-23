# coding: utf-8
from django.shortcuts import render, HttpResponse
from main.models import Product
import json
from .cart_items import Items


def cart(request):
    cart_items = []
    if request.session.get('items', False):
        items = request.session['items']
        for item in items:
            try:
                product = Product.objects.get(id=item['id'])
                product.count = item['count']
                cart_items.append(product)
            except Exception:
                continue
    return render(request, 'cart.html', {'cart_items': cart_items})


def add_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id', '')
        item = Items(request)
        alert = item.add_item(request, int(item_id))
    else:
        alert = 'error'
    return HttpResponse(json.dumps({'alert': alert}), content_type="application/json")


def del_item(request):
    if request.method == 'POST':
        item_position = request.POST.get('item_position', '')
        item = Items(request)
        alert = item.delete_item(request, int(item_position))
    else:
        alert = 'error'
    return HttpResponse(json.dumps({'alert': alert}), content_type="application/json")


def change_item_count(request):
    if request.method == 'POST':
        item_position = request.POST.get('item_position', '')
        item_count = request.POST.get('count', '')
        item = Items(request)
        alert = item.change_count(request, int(item_position), int(item_count))
    else:
        alert = 'error'
    return HttpResponse(json.dumps({'alert': alert}), content_type="application/json")