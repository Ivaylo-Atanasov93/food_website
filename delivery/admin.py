from django.contrib import admin

# Register your models here.
from delivery.models import DeliveryPrice


class DeliveryPriceAdmin(admin.ModelAdmin):
    list_display = ('price',)


admin.site.register(DeliveryPrice, DeliveryPriceAdmin)
