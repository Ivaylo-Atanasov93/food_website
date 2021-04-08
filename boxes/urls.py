from django.urls import path

from .views import create_or_update_box

urlpatterns = [
    path('create_box/', create_or_update_box, name='create_box'),
]
