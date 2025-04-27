from django.http import HttpResponse
from .models import Recipe


def recipes(request):
    recipes = Recipe.objects.all()
    return HttpResponse(recipes)

def recipeDetails(request, id):
    recipe = Recipe.objects.get(id=id)
    return HttpResponse(recipe.details())