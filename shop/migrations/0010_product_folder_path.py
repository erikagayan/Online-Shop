# Generated by Django 5.0 on 2024-01-12 10:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0009_alter_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="folder_path",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
