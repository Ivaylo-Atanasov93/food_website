from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from recipes.models import Recipe
from users.forms import UserAdminCreationForm


class CreateAccountPage(CreateView):
    queryset = Recipe.objects.all()
    template_name = 'sign_up.html'
    form_class = UserAdminCreationForm

    def form_valid(self, form):
        return super().form_valid(form)
