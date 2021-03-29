from django.shortcuts import render


# Create your views here.
from recipes.models import Recipe


def recipes(request):
    products = Recipe.objects.all()
    context = {
        'products': products
    }
    return render(request, 'recipes.html', context)

