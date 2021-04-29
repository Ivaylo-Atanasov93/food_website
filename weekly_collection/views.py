from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

from boxes.models import Box, ChoseMeals
from orders.models import Order, OrderItem
from recipes.models import Recipe, Ingredient
from weekly_collection.models import WeeklyCollection


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    added_ingredients = recipe.addingredient_set.all()
    ingredient_names = [added_ingredient.ingredient for added_ingredient in added_ingredients]
    ingredients = [Ingredient.objects.get(name=ingredient_names[i]) for i in range(len(ingredient_names))]
    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'recipe_details.html', context)


def recipes(request):
    if request.user.is_authenticated:
        customer = request.user.customer.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.get_total_items
        box = customer.box_set.get_or_create(customer=customer, complete_value=False)[0]
        chosen_meals = box.chosemeals_set.all()
        meal_ids = [meal.recipe.id for meal in chosen_meals]
        meal_quantity = range(1, box.get_meals_number + 1)

    else:
        order = {'get_total_items': 0, 'get_total_price': 0}
        cart_items = order['get_total_items']
        box = ''
        chosen_meals = ''
        meal_ids = []
        meal_quantity = range(1, 6)

    weekly_collection = WeeklyCollection.objects.filter(active=True)[0]
    recipe_list = [added_recipe.recipe for added_recipe in weekly_collection.addrecipe_set.all()]
    context = {
        'box': box,
        'recipes': recipe_list,
        'cart_items': cart_items,
        'meals': chosen_meals,
        'meal_ids': meal_ids,
        'meal_quantity': meal_quantity,
    }
    return render(request, 'recipes.html', context)


def update_box(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    customer = request.user.customer.user
    meal = Recipe.objects.get(id=product_id)

    box, created = Box.objects.get_or_create(customer=customer, complete_value=False)
    chose_meal, created = ChoseMeals.objects.get_or_create(box=box, recipe=meal)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=box, quantity=1)
    order_item.save()

    if action == 'add':
        box.chosemeals_set.add(chose_meal)
    elif action == 'remove':
        box.chosemeals_set.remove(chose_meal)

    return JsonResponse('Item was added', safe=False)
