from django.db import models
from django.urls import reverse
# from django_dropbox_storage.storage import DropboxStorage

# DROPBOX_STORAGE = DropboxStorage()
# Create your models here.
LEVEL_COOK = (('Легко','Легко'),('Легко','Средняя'),('Легко','Тяжёлая'))
QUANTITY_TYPE =(('г','г'),('шт','шт'),('мл','мл'),(None,"Нет меры")) 
class CategoryRecipe(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        pass

class Recipe(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=100)
    category_recipe = models.ForeignKey('CategoryRecipe', 
        on_delete=models.PROTECT, 
        related_name='recipes')
    description = models.TextField(max_length=3000)
    image = models.ImageField(upload_to="recipe_main_images/%Y/%m/%d/",
        # storage=DROPBOX_STORAGE
        )
    level = models.CharField(max_length=8, 
        choices=LEVEL_COOK,
        default="Легко" )
    time = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('recipe', args=[self.id])

    def __str__(self):
        return self.name

    def hours(self):
        time = self.time
        return '{} ч {} мин '.format(str(time//60) if time>=60 else 0,str(time%60))
    
    class Meta:
        pass

class RecipeImage(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="recipe_images/%Y/%m/%d/")
    recipe = models.ForeignKey('Recipe',on_delete=models.CASCADE, related_name="recipe_images")


class IngredientTemplate(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=50)
    quatity = models.CharField(max_length=50, choices = QUANTITY_TYPE,default=None)
    
    def __str__(self):
        return '%s,%s' % (self.name,self.quatity)

    class Meta:
        pass 

class Ingredient(models.Model):
    """
    Description: Model Description
    """
    ingeredient = models.ForeignKey('IngredientTemplate', 
        on_delete=models.CASCADE, related_name="instance_ingr")
    recipe = models.ForeignKey(
        'Recipe',
        on_delete = models.CASCADE,
        related_name = "ingredients"
        )
    count = models.IntegerField()

    def __str__(self):
        return self.ingeredient.name

    def full_display(self):
        count = self.count
        quatity = self.ingeredient.quatity
        if quatity == 'шт' or not quatity:
            return '%s %s' % (count,quatity)
        else:
            amount = [count//1000,count%1000]
            if count>=1000:
                text = "%s кг" % (amount[0]) if quatity == 'г' else "%s л" % (amount[0])
            else:
                text = ""
            return text + ' %s %s'%(amount[1],quatity)    

    class Meta:
        pass