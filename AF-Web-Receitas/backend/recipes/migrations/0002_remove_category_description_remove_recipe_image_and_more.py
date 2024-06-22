# Generated by Django 5.0.6 on 2024-06-18 23:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.category'),
        ),
    ]
