# Generated by Django 3.0.2 on 2020-01-08 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=50, verbose_name='Temperature')),
                ('potasium', models.CharField(max_length=50, verbose_name='Potasium')),
                ('moisture', models.CharField(max_length=20, verbose_name='Moisture')),
                ('humidity', models.CharField(max_length=20, verbose_name='Humidity')),
                ('nitrogen', models.CharField(max_length=20, verbose_name='Nitrogen')),
                ('tds', models.CharField(max_length=50, verbose_name='TDS')),
                ('ph', models.CharField(max_length=50, verbose_name='P.H')),
                ('turbidity', models.CharField(max_length=50, verbose_name='Turbidity')),
                ('phosphorus', models.CharField(max_length=50, verbose_name='Phosphorus')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FarmerSensorData', to='Account.Farmer', verbose_name='Farmer')),
            ],
        ),
    ]
