# Generated by Django 5.1.4 on 2025-01-27 12:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0008_rename_country_attributesvalues_product_attributes"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ProductAttributeValue",
        ),
    ]
