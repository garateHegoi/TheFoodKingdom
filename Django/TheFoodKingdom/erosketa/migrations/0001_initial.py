# Generated by Django 4.1.1 on 2022-10-26 06:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('janaria', '0001_initial'),
        ('bezeroa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saskiak',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('kantitate_kopurua', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('janari_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='janaria.janariak')),
            ],
        ),
        migrations.CreateModel(
            name='Erosketak',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('eguna', models.DateField(null=True)),
                ('ordua', models.DateTimeField(null=True)),
                ('ordaintzeko_guztira', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('bezero_dni', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bezeroa.bezeroak')),
                ('saskia_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erosketa.saskiak')),
            ],
        ),
    ]