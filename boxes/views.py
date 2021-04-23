from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.views.decorators.http import require_POST, require_GET
from django.views.generic import DetailView

from boxes.models import Box
from boxes.forms import BoxForm
from orders.models import Order
from recipes.models import Recipe


def create_or_update_box(request):
    if request.user.is_authenticated:
        context = {}
        customer = request.user.customer.user
        box, create = Box.objects.update_or_create(customer=customer, complete_value=False)
        form = BoxForm(request.POST or None, instance=box)
        if form.is_valid():
            form.save()
            box.save()
            return redirect('recipes')
        order = customer.order_set.filter(complete=False)[0]
        cart_items = order.get_total_items
        context['form'] = form
        context['cart_items'] = cart_items
        return render(request, 'create_box.html', context)
    return render(request, 'unauthenticated.html')
