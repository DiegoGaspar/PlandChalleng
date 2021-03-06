# Generated by Django 3.1 on 2020-08-14 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obj', '0005_auto_20200814_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tyre',
            old_name='estado',
            new_name='estado_degradacao',
        ),
        migrations.CreateModel(
            name='Reabastecer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField()),
                ('quant_gas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pago', models.BooleanField(default=False)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obj.car')),
            ],
        ),
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField()),
                ('quant_gas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pago', models.BooleanField(default=False)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obj.car')),
            ],
        ),
    ]
