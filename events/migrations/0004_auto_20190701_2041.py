# Generated by Django 2.2.2 on 2019-07-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190701_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_request',
            name='name',
        ),
        migrations.AddField(
            model_name='user_request',
            name='first_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='user_request',
            name='last_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
