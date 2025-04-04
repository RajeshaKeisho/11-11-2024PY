# Generated by Django 5.0.1 on 2024-05-17 19:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('ELE', 'Electronics'), ('FUR', 'Furniture'), ('CLO', 'Clothing'), ('TOY', 'Toys'), ('OTH', 'Other')], max_length=3)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('in_stock', models.BooleanField(default=True)),
            ],
        ),
    ]
