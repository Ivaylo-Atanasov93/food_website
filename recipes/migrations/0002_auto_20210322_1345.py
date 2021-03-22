# Generated by Django 3.1.7 on 2021-03-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='step',
            old_name='photo_url',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='allergens',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='ingredient_quantity',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='allergen',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('M&V', 'Meat and Vegie'), ('VRN', 'Vegetarian'), ('VGN', 'Vegan')], max_length=20),
        ),
        migrations.DeleteModel(
            name='IngredientQuantity',
        ),
    ]
