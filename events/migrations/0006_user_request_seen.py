# Generated by Django 2.2.2 on 2019-07-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190702_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_request',
            name='seen',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
