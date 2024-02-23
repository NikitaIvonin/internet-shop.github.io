# Generated by Django 5.0.2 on 2024-02-22 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_store', '0004_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auto_store.product')),
            ],
        ),
    ]
