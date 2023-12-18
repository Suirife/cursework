# Generated by Django 5.0 on 2023-12-18 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_orderitems_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderreport',
            name='order',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='order_report', to='main.orders'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='main.orders'),
        ),
    ]
