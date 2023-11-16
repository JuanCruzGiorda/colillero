# Generated by Django 4.2.6 on 2023-11-16 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colillero_project', '0004_alter_colillero_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='colillero',
            name='ip',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='colillero',
            name='estado',
            field=models.CharField(choices=[('vacio', 'Vacío'), ('porllenarse', 'Porllenarse'), ('lleno', 'Lleno')], default='vacio', max_length=20),
        ),
    ]
