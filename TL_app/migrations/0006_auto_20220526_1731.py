# Generated by Django 3.1.14 on 2022-05-26 08:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TL_app', '0005_auto_20220526_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='TL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TL_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='tle',
            name='end_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='tle',
            name='start_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='tle',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
