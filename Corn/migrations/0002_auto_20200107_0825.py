# Generated by Django 3.0.2 on 2020-01-07 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
        ('Corn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corn',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FarmerUploadsCorn', to='Account.Farmer', verbose_name='Farmer'),
        ),
    ]
