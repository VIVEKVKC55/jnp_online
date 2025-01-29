# Generated by Django 5.1.5 on 2025-01-29 12:03

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimages",
            name="full_url",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="product_photos"
            ),
        ),
    ]
