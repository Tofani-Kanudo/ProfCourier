# Generated by Django 2.2 on 2020-04-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0009_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='destination',
            field=models.CharField(max_length=15, null=True),
        ),
    ]