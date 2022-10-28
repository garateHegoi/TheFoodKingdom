# Generated by Django 4.1.1 on 2022-10-28 07:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bezeroa', '0007_alter_bezeroak_telefono_zenbakia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bezeroak',
            name='telefono_zenbakia',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator('^\\+?(6\\d{2}|34[1-9]\\d{1})\\d{6}$')]),
        ),
    ]