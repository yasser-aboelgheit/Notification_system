# Generated by Django 2.2.17 on 2021-01-31 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='text_ar',
            new_name='text_arr',
        ),
    ]