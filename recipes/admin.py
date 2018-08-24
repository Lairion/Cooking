from django.contrib import admin
from .models import (RecipeImage,
    Recipe,
    CategoryRecipe,
    Ingredient,
    IngredientTemplate)
from .form import IngredientForm,RecipeForm

class IngerdientTemplateAdmin(admin.ModelAdmin):
    '''
        Admin View for Ingerdient
    '''
    list_display = ('name','quatity',)
    list_filter = ('name','quatity',)
    search_fields = ('name',)

admin.site.register(IngredientTemplate, IngerdientTemplateAdmin)

class CategoryRecipeAdmin(admin.ModelAdmin):
    '''
        Admin View for CategoryRecipe
    '''
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(CategoryRecipe, CategoryRecipeAdmin)

class IngredientInline(admin.TabularInline):
    '''
        Tabular Inline View for Ingredient
    '''
    model = Ingredient
    form = IngredientForm


class RecipeImageInline(admin.TabularInline):
    '''
        Tabular Inline View for RecipeImage
    '''
    model = RecipeImage

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    '''
        Admin View for Recipe
    '''
    list_display = ('name',)
    list_filter = ('category_recipe',)
    inlines = [
        IngredientInline,
        RecipeImageInline,
    ]
    search_fields = ('name',)
    form = RecipeForm

admin.site.register(Recipe, RecipeAdmin)

