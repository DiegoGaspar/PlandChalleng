# Generated by Django 3.1 on 2020-08-14 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obj', '0006_auto_20200814_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='pneus',
        ),
        migrations.AddField(
            model_name='tyre',
            name='carro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='obj.car'),
            preserve_default=False,
        ),
    ]