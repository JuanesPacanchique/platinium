# Generated by Django 4.2.7 on 2023-12-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='N_Producto',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='productos',
            name='Precio',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
