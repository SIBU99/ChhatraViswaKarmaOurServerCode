# Generated by Django 3.0.2 on 2020-01-07 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Corn', '0002_auto_20200107_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corn',
            name='healthy',
        ),
    ]
