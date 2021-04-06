from django.contrib import admin
from .models import OrderItem, DeliveryInformation, Order


# Register your models here

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_ordered', 'complete', 'transaction_id')
    list_filter = ('customer', 'date_ordered', 'complete')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')
    list_filter = ('product', 'order', 'quantity', 'date_added')


class DeliveryInformationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'city', 'day_added')
    list_filter = ('customer', 'order', 'city', 'day_added')


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryInformation)
