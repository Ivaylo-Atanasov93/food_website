from django.urls import path

from users.views import login_view, sign_up_view

urlpatterns = [
    path('', login_view, name='login'),
    path('sign_up/', sign_up_view, name='sign_up'),
]
