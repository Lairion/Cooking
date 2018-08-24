from dal import autocomplete

from django import forms
from .models import Ingredient,Recipe

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('__all__')
        widgets = {
            'ingeredient': autocomplete.ModelSelect2(
                url='ing_temp_comp'
                )
        }
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('__all__')
        widgets = {
            'category_recipe': autocomplete.ModelSelect2(
                url='recipes_categories'
                )
        }