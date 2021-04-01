import json

from django.http import JsonResponse
from django.shortcuts import render
import datetime

# Create your views here.
from orders.models import Order, DeliveryInformation
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
        delivery_price = DeliveryPrice.objects.all()[0].price

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


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        if total == order.get_total_price:
            order.complete = True
        order.save()
        if order.is_shipping:
            DeliveryInformation.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                postcode=data['shipping']['postcode'],
                phone_number=data['shipping']['phone_number'],
                day_added=[],
            )
    else:
        print('User is not logged in!')
    return JsonResponse('Payment complete!', safe=False)
