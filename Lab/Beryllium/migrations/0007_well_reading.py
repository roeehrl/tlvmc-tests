# Generated by Django 3.2.6 on 2021-08-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beryllium', '0006_plate_populated'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='reading',
            field=models.FloatField(default=0),
        ),
    ]
