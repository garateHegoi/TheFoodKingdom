# Generated by Django 4.1.1 on 2022-11-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bezeroa', '0003_bezeroak_puntuak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bezeroak',
            name='puntuak',
            field=models.IntegerField(default=0),
        ),
    ]
