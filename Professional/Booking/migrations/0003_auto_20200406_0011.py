# Generated by Django 2.2 on 2020-04-05 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0002_auto_20200406_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_user',
            name='admin',
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='p_user',
            name='branches',
            field=models.ForeignKey(blank=True, default='JNR', on_delete=django.db.models.deletion.CASCADE, to='Booking.branch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='p_user',
            name='origin',
            field=models.ForeignKey(blank=True, default='JNR', on_delete=django.db.models.deletion.CASCADE, to='Booking.origin'),
            preserve_default=False,
        ),
    ]
