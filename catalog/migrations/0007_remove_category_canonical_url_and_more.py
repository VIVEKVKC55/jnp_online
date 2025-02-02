# Generated by Django 5.1.5 on 2025-02-01 07:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0006_product_other_brand"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="canonical_url",
        ),
        migrations.RemoveField(
            model_name="category",
            name="image_alt_tag",
        ),
        migrations.RemoveField(
            model_name="category",
            name="image_title",
        ),
        migrations.AddField(
            model_name="category",
            name="include_in_menu",
            field=models.BooleanField(default=False),
        ),
    ]
