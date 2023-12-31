# Generated by Django 5.0 on 2023-12-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('completed', 'completed'), ('cancelled', 'cancelled')], default='active', max_length=255),
        ),
        migrations.AlterField(
            model_name='orders',
            name='type',
            field=models.CharField(choices=[('online', 'online'), ('offline', 'offline')], default='offline', max_length=255),
        ),
    ]
