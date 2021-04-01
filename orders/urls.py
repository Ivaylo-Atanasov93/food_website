from django.urls import path
from .views import cart, checkout, process_order

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('process_order/', process_order, name='process_order'),
]
