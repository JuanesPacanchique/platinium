# Generated by Django 5.0 on 2023-12-12 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqrs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pqrs',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='pqrs',
            name='opcion',
            field=models.CharField(choices=[('pregunta', 'Pregunta'), ('queja', 'Queja'), ('reclamo', 'Reclamo'), ('sugerencia', 'Sugerencia')], max_length=20, null=True),
        ),
    ]
