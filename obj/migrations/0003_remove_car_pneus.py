# Generated by Django 3.1 on 2020-08-14 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obj', '0002_car_pneus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='pneus',
        ),
    ]