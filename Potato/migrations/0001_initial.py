# Generated by Django 3.0.2 on 2020-01-07 13:44

import Potato.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Potato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=Potato.models.upload_potato, verbose_name='Image Uploaded')),
                ('result_tag', models.BooleanField(default=False, editable=False, verbose_name='Proceed')),
                ('disease1', models.FloatField(blank=True, default=0.0, verbose_name='Gray Leaf Spot')),
                ('disease2', models.FloatField(blank=True, default=0.0, verbose_name='Common Rust')),
                ('when', models.DateTimeField(auto_now_add=True, help_text='When the image is  uploaded', verbose_name='Added On')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FarmerUploadsPotato', to='Account.Farmer', verbose_name='Farmer')),
            ],
            options={
                'verbose_name': 'Potato',
                'verbose_name_plural': 'Potatoes',
            },
        ),
    ]
