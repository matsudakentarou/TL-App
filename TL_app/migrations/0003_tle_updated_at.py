# Generated by Django 3.1.14 on 2022-05-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TL_app', '0002_tle_importance'),
    ]

    operations = [
        migrations.AddField(
            model_name='tle',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
    ]
