# Generated by Django 5.1.5 on 2025-01-29 12:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_alter_productimages_full_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image_url",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="category"
            ),
        ),
        migrations.AlterField(
            model_name="productbrand",
            name="image_url",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="brand"
            ),
        ),
    ]
