# Generated by Django 2.2.2 on 2019-06-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_theme', models.CharField(choices=[('cocktail party', 'Cocktail Party'), ('kitty party', 'Kitty Party'), ('pool party', 'Pool Party'), ('dj night', 'DJ Night'), ('bachlor party', 'Bachlor Party'), ('welcome & Farewell party', 'Welcome & Farewell Party'), ('fashion show', 'Fashion Show')], max_length=100)),
                ('description', models.CharField(blank=True, default=None, max_length=500)),
                ('party_file', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decoration', models.CharField(choices=[('balloon decoration', 'Balloon Decoration'), ('flower decoration', 'Flower Decoration'), ('mall decoration', 'Mall Decoration'), ('showroom decoration', 'Showroom Decoration'), ('festival theme decoration', 'Festival Theme Decoration')], max_length=100)),
                ('description', models.CharField(blank=True, default=None, max_length=500)),
                ('decoration_file', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(choices=[('education event', 'Education Event'), ('automobile event', 'Automobile Event'), ('electronic gadget event', 'Electronic Gadget Event'), ('health event', 'Health Product Event'), ('beauty event', 'Beauty Product Event')], default=None, max_length=100)),
                ('description', models.CharField(blank=True, default=None, max_length=500)),
                ('event_file', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='User_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.IntegerField()),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]
