from django.urls import path

from sales.views import sales_stats_view

urlpatterns = [
    path('', sales_stats_view, name='sales')
]
