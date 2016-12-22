from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def product(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'product.html', context)


