# Generated by Django 2.2 on 2020-04-05 17:41

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('branch', models.CharField(max_length=3, null=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('pincode', models.IntegerField(primary_key=True, serialize=False)),
                ('district', models.CharField(max_length=40, null=True)),
                ('state', models.CharField(max_length=40, null=True)),
            ],
            options={
                'db_table': 'Location',
            },
        ),
        migrations.CreateModel(
            name='origin',
            fields=[
                ('origin', models.CharField(max_length=3, null=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Origin',
            },
        ),
        migrations.CreateModel(
            name='party',
            fields=[
                ('number', models.CharField(max_length=13, null=True, primary_key=True, serialize=False, unique=True)),
                ('reference', models.CharField(blank=True, max_length=13, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('name', models.CharField(max_length=40, null=True)),
                ('address1', models.CharField(max_length=500, null=True)),
                ('address2', models.CharField(max_length=500, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('gst', models.CharField(blank=True, max_length=15, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Party',
            },
        ),
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_local', models.IntegerField(null=True)),
                ('first_sau', models.IntegerField(null=True)),
                ('first_guj', models.IntegerField(null=True)),
                ('first_west', models.IntegerField(null=True)),
                ('first_metro', models.IntegerField(null=True)),
                ('first_ROI', models.IntegerField(null=True)),
                ('first_spec', models.IntegerField(null=True)),
                ('local', models.IntegerField()),
                ('sau', models.IntegerField()),
                ('guj', models.IntegerField()),
                ('west', models.IntegerField()),
                ('metro', models.IntegerField()),
                ('ROI', models.IntegerField()),
                ('spec', models.IntegerField()),
            ],
            options={
                'db_table': 'Price',
            },
        ),
        migrations.CreateModel(
            name='p_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('admin', models.BooleanField(blank=True)),
                ('branches', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.branch')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('origin', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.origin')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Prof_Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.party')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.price')),
            ],
            options={
                'db_table': 'C_ship',
            },
        ),
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Content',
            },
        ),
        migrations.AddField(
            model_name='branch',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.origin'),
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('pod', models.CharField(max_length=11, null=True, primary_key=True, serialize=False, unique=True)),
                ('booktype', models.CharField(max_length=6, null=True)),
                ('branch', models.CharField(max_length=3, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('destination', models.CharField(max_length=3, null=True)),
                ('nop', models.IntegerField()),
                ('weight', models.CharField(max_length=11, null=True)),
                ('amount', models.CharField(max_length=11, null=True)),
                ('value', models.CharField(blank=True, max_length=11, null=True)),
                ('content', models.CharField(blank=True, max_length=100, null=True)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='Booking.party')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='Booking.party')),
            ],
            options={
                'db_table': 'Booking',
            },
        ),
        migrations.CreateModel(
            name='apod',
            fields=[
                ('apod', models.CharField(max_length=11, null=True, primary_key=True, serialize=False, unique=True)),
                ('p_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'allocated_pod',
            },
        ),
    ]