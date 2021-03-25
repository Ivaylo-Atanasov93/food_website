from django.urls import path
from .views import cart, checkout

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]