from django.contrib import admin

# Register your models here.
from weekly_collection.models import AddRecipe, WeeklyCollection


class AddRecipeInLine(admin.StackedInline):
    model = AddRecipe
    extra = 0


class WeeklyCollectionAdmin(admin.ModelAdmin):
    list_display = ('week_start', 'week_end', 'active')
    list_filter = ('week_start', 'week_end', 'active')
    inlines = [
        AddRecipeInLine,
    ]


admin.site.register(WeeklyCollection, WeeklyCollectionAdmin)
admin.site.register(AddRecipe)
