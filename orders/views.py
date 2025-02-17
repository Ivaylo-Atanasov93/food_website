import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
import datetime

# Create your views here.
from manjorno_v3.decorators import allowed_users
from orders.models import Order, DeliveryInformation
from prices.models import DeliveryPrice


@allowed_users(allowed_roles=['customer', 'delivery', 'admin'])
def user_orders_view(request):
    context = {}
    user = request.user.customer.user
    orders = user.order_set.filter(complete=True)
    order = user.order_set.filter(complete=False)[0]
    cart_items = order.get_total_items
    context['cart_items'] = cart_items
    context['orders'] = orders
    return render(request, 'orders.html', context)


@allowed_users(allowed_roles=['customer', 'delivery', 'admin'])
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_total_items
        if cart_items == 0:
            return redirect('create_box')
        delivery_price = DeliveryPrice.objects.all()[0].price
    else:
        items = []
        order = {'get_total_items': 0, 'get_total_price': 0}
        cart_items = order['get_total_items']
        delivery_price = DeliveryPrice.objects.all()[0].price

    context = {
        'items': items,
        'order': order,
        'cart_items': cart_items,
        'delivery_price': delivery_price
    }
    return render(request, 'cart.html', context)

@allowed_users(allowed_roles=['customer', 'delivery', 'admin'])
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
        box = customer.box_set.get_or_create(customer=customer, complete_value=False)[0]
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_total_price:
            order.complete = True
            box.complete_value = True

        order.save()
        box.save()

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
