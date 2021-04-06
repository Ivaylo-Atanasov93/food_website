from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

# Create your views here.
from django.views.generic import DetailView, CreateView

from boxes.models import Box
from boxes.forms import BoxForm
from recipes.models import Recipe


class CreateBoxView(LoginRequiredMixin, CreateView):
    template_name = 'create_box.html'
    form_class = BoxForm

    def form_valid(self, form):
        return super().form_valid(form)


class BoxDetailView(LoginRequiredMixin, DetailView):
    template_name = 'box_details.html'

    def get_queryset(self):
        queryset = {Recipe.objects.all()}
        return queryset

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Box, id=id_)

