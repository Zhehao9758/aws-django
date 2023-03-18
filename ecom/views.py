from django.contrib import messages
from django.shortcuts import render, redirect

from ecom.models import Product, Cart


def index(request):
    products = Product.objects.all()
    print(len(products))
    for product in products:
        product.price = float(product.price) / 100
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    product.price = float(product.price) / 100
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)


def cart(request):
    carts = Cart.objects.all()
    total = 0
    for order in carts:
        order.product.price = float(order.product.price * order.quantity) / 100
        total += order.product.price
    context = {
        'carts': carts,
        'total': total
    }
    return render(request, 'cart.html', context)


def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    order, created = Cart.objects.get_or_create(product=product)
    if not created:
        order.quantity += 1
    order.save()
    messages.success(request, "was added to your cart.")
    return redirect("/ecom")


def incre(request, pk):
    product = Product.objects.get(pk=pk)
    order = Cart.objects.get(product=product)
    order.quantity += 1
    order.save()
    return redirect("/ecom/cart")


def decre(request, pk):
    product = Product.objects.get(pk=pk)
    order = Cart.objects.get(product=product)
    if order.quantity == 1:
        order.delete()
    else:
        order.quantity -= 1
        order.save()
    return redirect("/ecom/cart")


def delete(request, pk):
    product = Product.objects.get(pk=pk)
    order = Cart.objects.get(product=product)
    order.delete()
    return redirect("/ecom/cart")
