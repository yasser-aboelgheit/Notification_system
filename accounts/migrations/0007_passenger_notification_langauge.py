# Generated by Django 2.2.17 on 2021-01-31 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210130_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='notification_langauge',
            field=models.IntegerField(choices=[(0, 'english'), (1, 'arabic')], default=0),
        ),
    ]
