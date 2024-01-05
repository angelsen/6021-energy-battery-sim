# Generated by Django 5.0.1 on 2024-01-04 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DutyCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('duty_cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hps_EnergySim.dutycycle')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingLoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load_type', models.CharField(max_length=100)),
                ('load_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duty_cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hps_EnergySim.dutycycle')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('duty_cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hps_EnergySim.dutycycle')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hps_EnergySim.location')),
                ('operating_loads', models.ManyToManyField(blank=True, to='hps_EnergySim.operatingload')),
            ],
        ),
        migrations.AddField(
            model_name='dutycycle',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hps_EnergySim.project'),
        ),
    ]