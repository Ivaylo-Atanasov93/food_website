from django.contrib import admin
from .models import Recipe, Step, Ingredient, AddIngredient, BaseMealPrice


# Register your models here.
class BaseMealPriceAdmin(admin.ModelAdmin):
    list_display = ('price',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'allergen')
    list_filter = ('name', 'allergen')


class StepAdmin(admin.ModelAdmin):
    list_display = ('description',)
    list_filter = ('description',)


class StepInLine(admin.StackedInline):
    model = Step
    extra = 0


class IngredientQuantityInLine(admin.StackedInline):
    model = AddIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'difficulty', 'cooking_time', 'origin')
    list_filter = ('type', 'difficulty', 'cooking_time')
    inlines = [
        StepInLine,
        IngredientQuantityInLine,
    ]


admin.site.register(BaseMealPrice, BaseMealPriceAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Ingredient, IngredientAdmin)
