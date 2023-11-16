# Generated by Django 4.2.6 on 2023-11-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colillero_project', '0002_colillero_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colillero',
            name='estado',
            field=models.CharField(choices=[('vacio', 'Vacio'), ('porLlenarse', 'PorLlenarse'), ('lleno', 'Lleno')], max_length=20),
        ),
    ]