# Generated by Django 5.0 on 2023-12-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_orders_status_alter_orders_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
