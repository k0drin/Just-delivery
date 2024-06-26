# Generated by Django 5.0.4 on 2024-04-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_category_delete_order_delete_restaurant"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="Appetizers",
            new_name="title",
        ),
        migrations.RemoveField(
            model_name="category",
            name="Desserts",
        ),
        migrations.RemoveField(
            model_name="category",
            name="Drinks",
        ),
        migrations.RemoveField(
            model_name="category",
            name="Entrees",
        ),
        migrations.RemoveField(
            model_name="category",
            name="Sides",
        ),
        migrations.RemoveField(
            model_name="category",
            name="name",
        ),
        migrations.AddField(
            model_name="category",
            name="description",
            field=models.CharField(default="example description", max_length=1000),
            preserve_default=False,
        ),
    ]
