from django.contrib import admin
from .models import Recipe, Step, Ingredient, IngredientQuantity


# Register your models here.


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'allergen')
    list_filter = ('name', 'allergen')


class IngredientQuantityAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'quantity')
    list_filter = ('ingredient',)


class StepAdmin(admin.ModelAdmin):
    list_display = ('description',)
    list_filter = ('description',)


class StepInLine(admin.StackedInline):
    model = Step
    extra = 0


class IngredientQuantityInLine(admin.StackedInline):
    model = IngredientQuantity
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'difficulty', 'cooking_time', 'origin')
    list_filter = ('type', 'difficulty', 'cooking_time')
    inlines = [
        StepInLine,
        IngredientQuantityInLine,
    ]


admin.site.register(IngredientQuantity, IngredientQuantityAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Ingredient, IngredientAdmin)
