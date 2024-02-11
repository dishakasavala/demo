# Generated by Django 5.0 on 2024-01-01 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_remove_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.enter')),
            ],
        ),
    ]
