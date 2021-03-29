from django.shortcuts import render

# Create your views here.
from orders.models import Order


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total_items': 0, 'get_total_price': 0}

    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total_items': 0, 'get_total_price': 0}

    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)
