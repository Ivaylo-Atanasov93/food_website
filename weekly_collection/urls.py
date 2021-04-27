from django.urls import path
from .views import recipes, update_box, recipe_details

urlpatterns = [
    path('', recipes, name='recipes'),
    path('details/<int:pk>/', recipe_details, name='recipe_details'),
    path('update_box/', update_box, name='update_box'),
]
