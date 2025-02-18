# Generated by Django 3.2.25 on 2025-01-03 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('time_minutes', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('instructions', models.TextField(verbose_name='Cooking Instructions')),
                ('category', models.CharField(choices=[('Dessert', 'Dessert'), ('Main Course', 'Main Course'), ('Appetizer', 'Appetizer'), ('Salad', 'Salad'), ('Soup', 'Soup'), ('Beverage', 'Beverage'), ('Snack', 'Snack')], default='Main Course', max_length=50, verbose_name='Category')),
                ('preparation_time', models.PositiveIntegerField(verbose_name='Preparation Time (minutes)')),
                ('cooking_time', models.PositiveIntegerField(verbose_name='Cooking Time (minutes)')),
                ('servings', models.PositiveIntegerField(verbose_name='Servings')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
