from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        orders = user.order_set.filter(complete=False)[0]
        cart_items = orders.get_total_items
        context['cart_items'] = cart_items
    else:
        order = {'get_total_items': 0, 'get_total_price': 0}
        cart_items = order['get_total_items']
        context['cart_items'] = cart_items
    return render(request, 'index.html', context)
