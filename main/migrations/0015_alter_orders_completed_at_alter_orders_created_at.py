# Generated by Django 5.0 on 2023-12-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_orderreport_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='completed_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
