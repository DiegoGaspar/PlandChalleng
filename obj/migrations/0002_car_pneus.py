# Generated by Django 3.1 on 2020-08-14 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='pneus',
            field=models.CharField(choices=[('pneu1', 'Tyre'), ('pneu2', 'Tyre')], default=1, max_length=5),
            preserve_default=False,
        ),
    ]