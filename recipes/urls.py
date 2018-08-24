from django.urls import path
from .views import RecipeViews
from .autocompletes import (
    IngredientTemplateAutocomplete,
    CategoryRecipeAutocomplete
    )
urlpatterns = [
    path('recipes_list/', 
        RecipeViews.recipes_list_view, 
        name="recipes_list" ),
    path('recipes_list/<int:id>', 
        RecipeViews.recipe_view, 
        name="recipe" ),
    path('ingeredient_templates/',
        IngredientTemplateAutocomplete.as_view(),
        name="ing_temp_comp"
        ),
    path('recipes_categories/',
        CategoryRecipeAutocomplete.as_view(),
        name="recipes_categories"
        )

]