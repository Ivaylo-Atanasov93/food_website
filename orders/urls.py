from django.urls import path
from .views import cart, checkout, process_order, user_orders_view

urlpatterns = [
    path('', cart, name='cart'),
    path('user_orders/', user_orders_view, name='user_orders'),
    path('checkout/', checkout, name='checkout'),
    path('process_order/', process_order, name='process_order'),
]
