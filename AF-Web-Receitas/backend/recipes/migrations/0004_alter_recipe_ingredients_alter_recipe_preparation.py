# Generated by Django 5.0.6 on 2024-06-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation',
            field=models.TextField(),
        ),
    ]
