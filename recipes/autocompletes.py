from dal import autocomplete

from .models import IngredientTemplate,CategoryRecipe


class IngredientTemplateAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return IngredientTemplate.objects.none()

        qs = IngredientTemplate.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class CategoryRecipeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return CategoryRecipe.objects.none()

        qs = CategoryRecipe.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs