from django.urls import path

from .views import CreateBoxView, BoxDetailView

urlpatterns = [
    path('create_box/', CreateBoxView.as_view(), name='create_box'),
    path('create_box/<int:id>/', BoxDetailView.as_view(), name='box_details'),
]
