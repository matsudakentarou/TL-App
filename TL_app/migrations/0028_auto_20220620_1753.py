# Generated by Django 3.1.14 on 2022-06-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TL_app', '0027_tle_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='tle',
            name='map',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tle',
            name='video',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tle',
            name='body',
            field=models.TextField(default=''),
        ),
    ]
