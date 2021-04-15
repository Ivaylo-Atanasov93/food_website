from django.urls import path

from users.views import login_view, sign_up_view, logout_view, user_profile_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign_up/', sign_up_view, name='sign_up'),
    path('profile/', user_profile_view, name='profile'),
]
