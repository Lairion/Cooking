from django.urls import path
from .views import RecipeViews
urlpatterns = [
    path('recipes_list/', 
    	RecipeViews.recipes_list_view, 
    	name="recipes_list" ),
    path('recipes_list/<int:id>', 
    	RecipeViews.recipe_view, 
    	name="recipe" ),
]