# Generated by Django 3.1.14 on 2022-06-02 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TL_app', '0014_auto_20220602_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='tl_year',
            name='parent',
            field=models.ManyToManyField(to='TL_app.TL'),
        ),
    ]