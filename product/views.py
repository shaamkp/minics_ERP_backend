from django.shortcuts import render
from product.models import Product, Cart


def product(request):
    products = Product.objects.all()

    context={
        "products": products
    }

    return render(request,"product.html",context=context)


def cart(request):
    carts = Cart.objects.all()

    context={
        "carts":carts
    }

    return render(request,"cart.html",context=context)
