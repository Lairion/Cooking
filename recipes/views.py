from django.shortcuts import render
from .models import Recipe,CategoryRecipe
from .filters import RecipeFilter
# Create your views here.

class RecipeViews(object):
    """docstring for RecipeView"""
    @staticmethod
    def recipes_list_view(request):
        filter_recipe = RecipeFilter(request.GET, queryset=Recipe.objects.all())
        recipes = Recipe.objects.all()
        categories = CategoryRecipe.objects.all()
        context = {
            'title':"Recipes list",
            'recipes': recipes,
            'categories':categories,
            'filter':filter_recipe
        }
        return render(request,"recipes_list_view.html",context)

    @staticmethod
    def recipe_view(request,id):
        recipe = Recipe.objects.get(id=id)
        context = {
            'title':"Recipes list",
            'recipe': recipe
        }
        return render(request,"recipe_view.html",context)