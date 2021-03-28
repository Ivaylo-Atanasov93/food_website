from django.contrib import admin
from .models import Box, ChoseMeals, OrderItem, DeliveryInformation, Order


# Register your models here


class ChosenMealsInLine(admin.StackedInline):
    model = ChoseMeals
    extra = 0


class BoxAdmin(admin.ModelAdmin):
    list_display = ('meal_size', 'number_of_meals',)
    list_filter = ('meal_size', 'number_of_meals',)
    inlines = [
        ChosenMealsInLine,
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_ordered', 'complete', 'transaction_id')
    list_filter = ('customer', 'date_ordered', 'complete')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')
    list_filter = ('product', 'order', 'quantity', 'date_added')


class DeliveryInformationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'city', 'day_added')
    list_filter = ('customer', 'order', 'city', 'day_added')


admin.site.register(Box, BoxAdmin)
admin.site.register(ChoseMeals)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryInformation)
