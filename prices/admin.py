from django.contrib import admin
from prices.models import DeliveryPrice, BaseMealPrice


# Register your models here.


class BaseMealPriceAdmin(admin.ModelAdmin):
    list_display = ('price',)


class DeliveryPriceAdmin(admin.ModelAdmin):
    list_display = ('price',)


admin.site.register(DeliveryPrice, DeliveryPriceAdmin)
admin.site.register(BaseMealPrice, BaseMealPriceAdmin)