# Generated by Django 4.0 on 2021-12-29 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_category_name'),
        ('store', '0002_alter_product_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='category.category'),
        ),
    ]
