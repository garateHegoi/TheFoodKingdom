# Generated by Django 4.1.1 on 2022-10-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidalketa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='txartelak',
            name='cvv',
            field=models.CharField(max_length=3),
        ),
    ]
