from django.contrib import admin
from .models import Box, ChoseMeals


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


admin.site.register(Box, BoxAdmin)
admin.site.register(ChoseMeals)
