from django.shortcuts import render

# Create your views here.
from manjorno_v3.decorators import allowed_users
from orders.models import Order


@allowed_users(allowed_roles=['delivery', 'admin'])
def sales_stats_view(request):
    sales = Order.objects.filter(complete=True)
    context = {
        sales: 'sales',
    }
    return render(request, 'sales.html', context)
