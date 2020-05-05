# Generated by Django 2.2 on 2020-04-09 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0019_auto_20200409_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='air_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Air', to='Booking.price'),
        ),
        migrations.AddField(
            model_name='party',
            name='sur_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surface', to='Booking.price'),
        ),
    ]