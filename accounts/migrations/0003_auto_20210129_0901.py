# Generated by Django 2.2.17 on 2021-01-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210129_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='driver_license_number',
            field=models.CharField(default=' ', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='driver',
            name='years_of_experience',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='passenger',
            name='home_address',
            field=models.CharField(default=' ', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='passenger',
            name='work_address',
            field=models.CharField(default=' ', max_length=128),
            preserve_default=False,
        ),
    ]