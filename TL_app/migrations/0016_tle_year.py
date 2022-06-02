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
<<<<<<< HEAD
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='TL_app.year'),
            preserve_default=False,
=======
            field=models.ForeignKey(default=1800, on_delete=django.db.models.deletion.DO_NOTHING, to='TL_app.tl_year'),
>>>>>>> dd8416c3aebdffd5ab6cf222807d61fbb924d9ac
        ),
    ]
