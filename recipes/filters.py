import django_filters

class RecipeFilter(django_filters.FilterSet):
	count__gt = django_filters.NumberFilter(
		field_name='price', 
		lookup_expr='gt'
		)
	count__lt = django_filters.NumberFilter(
		field_name='price',
		lookup_expr='lt'
		)
	time__gt = django_filters.NumberFilter(
		field_name='price', 
		lookup_expr='gt'
		)
	time__lt = django_filters.NumberFilter(
		field_name='price',
		lookup_expr='lt'
		)
    class Meta:
        model = Recipe
        fields = ['name','category_recipe','count','time']