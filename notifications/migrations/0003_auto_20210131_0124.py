# Generated by Django 2.2.17 on 2021-01-31 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20210131_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='text_arr',
            new_name='text_ar',
        ),
    ]
