# Generated by Django 3.2.9 on 2021-11-02 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('populated', models.PositiveSmallIntegerField(choices=[(1, 'populated'), (2, 'empty')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Plate_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.PositiveSmallIntegerField(choices=[(1, 'test'), (2, 'control')], default=1)),
                ('days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Test_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numInPlate', models.IntegerField()),
                ('numInTest', models.IntegerField(null=True)),
                ('row', models.IntegerField(null=True)),
                ('column', models.IntegerField(null=True)),
                ('isActive', models.BooleanField()),
                ('dosage', models.FloatField()),
                ('unitOfMeasure', models.CharField(default='mg', max_length=200)),
                ('reading', models.FloatField(default=0)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Beryllium.material')),
                ('plate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Beryllium.plate')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=1000)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Beryllium.patient')),
                ('tester', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Beryllium.tester')),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Beryllium.test_type')),
            ],
        ),
        migrations.AddField(
            model_name='plate',
            name='plate_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Beryllium.plate_type'),
        ),
        migrations.AddField(
            model_name='plate',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Beryllium.test'),
        ),
    ]
