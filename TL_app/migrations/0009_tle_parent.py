# Generated by Django 3.1.14 on 2022-05-26 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TL_app', '0008_auto_20220526_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='tle',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TL_app.tl', verbose_name=''),
        ),
    ]
