# Generated by Django 2.2.17 on 2021-01-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_passenger_national_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='failed_attempts',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='failed_attempts',
        ),
        migrations.AddField(
            model_name='driver',
            name='name',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='name',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
    ]
