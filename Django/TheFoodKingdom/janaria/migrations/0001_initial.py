# Generated by Django 4.1.1 on 2022-10-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Janariak',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('izena', models.CharField(max_length=50)),
                ('osagaiak', models.CharField(max_length=100)),
                ('prezioa', models.CharField(max_length=5)),
                ('mota', models.CharField(max_length=50)),
                ('alergenoak', models.CharField(max_length=50)),
                ('argazki_url', models.CharField(max_length=255)),
            ],
        ),
    ]
