# Generated by Django 4.0 on 2021-12-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_variation'),
        ('carts', '0002_cartitem_delete_cartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
