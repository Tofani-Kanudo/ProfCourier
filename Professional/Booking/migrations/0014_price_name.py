# Generated by Django 2.2 on 2020-04-08 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0013_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.party'),
        ),
    ]
