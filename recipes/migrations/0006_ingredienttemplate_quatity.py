# Generated by Django 2.1 on 2018-08-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20180811_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredienttemplate',
            name='quatity',
            field=models.CharField(choices=[('г', 'г'), ('шт', 'шт'), ('мл', 'мл'), (None, 'Нет меры')], default=None, max_length=50),
        ),
    ]
