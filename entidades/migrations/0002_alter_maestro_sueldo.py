# Generated by Django 5.0.6 on 2024-05-15 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestro',
            name='sueldo',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=8),
        ),
    ]
