from django.contrib import admin

# Register your models here.
from boxes.models import ChoseMeals, Box


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
