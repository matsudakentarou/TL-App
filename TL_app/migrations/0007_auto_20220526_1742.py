# Generated by Django 3.1.14 on 2022-05-26 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TL_app', '0006_auto_20220526_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tl',
            old_name='TL_title',
            new_name='title',
        ),
    ]
