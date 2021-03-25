from django.urls import path
from .views import recipes
urlpatterns = [
    path('', recipes, name='recipes')
]
