# Generated by Django 3.2.6 on 2021-08-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beryllium', '0005_well_unitofmeasure'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='populated',
            field=models.PositiveSmallIntegerField(choices=[(1, 'populated'), (2, 'empty')], default=2),
        ),
    ]
