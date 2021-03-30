from django.shortcuts import render

# Create your views here.
from orders.models import Order
from prices.models import DeliveryPrice


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_total_items
        delivery_price = DeliveryPrice.objects.all()[0].price
    else:
        items = []
        order = {'get_total_items': 0, 'get_total_price': 0}
        cart_items = order['get_total_items']

    context = {'items': items, 'order': order, 'cart_items': cart_items, 'delivery_price': delivery_price}
    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_total_items
    else:
        items = []
        order = {'get_total_items': 0, 'get_total_price': 0}
        cart_items = order['get_total_items']

    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'checkout.html', context)
