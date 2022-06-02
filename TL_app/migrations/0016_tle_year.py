from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [

        ('TL_app', '0015_year_tl'),
        ('TL_app', '0015_tl_year_parent'),

    ]

    operations = [
        migrations.AddField(
            model_name='tle',
            name='year',
            
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='TL_app.year'),
            preserve_default=False,

        ),
    ]
