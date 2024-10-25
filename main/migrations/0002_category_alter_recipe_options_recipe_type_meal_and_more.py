# Generated by Django 5.1.1 on 2024-10-25 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='наименование категории')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
            ],
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'рецепт', 'verbose_name_plural': 'рецепты'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='type_meal',
            field=models.CharField(blank=True, choices=[('BREAKFAST', 'завтрак'), ('LUNCH', 'обед'), ('DINNER', 'ужин'), ('SNACK', 'перекус'), ('BRUNCH', 'бранч'), ('SUPPER', 'поздний ужин'), ('TEA', 'чаепитие')], max_length=10, null=True, verbose_name='тип приема пищи'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='calories',
            field=models.IntegerField(blank=True, null=True, verbose_name='калории'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=225, verbose_name='название рецепта'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='категория'),
        ),
    ]
