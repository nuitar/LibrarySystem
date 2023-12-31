# Generated by Django 5.0 on 2023-12-21 09:11

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(unique=True)),
                ('category', models.CharField(max_length=10, unique=True)),
                ('per_day_fine', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='BookManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=20)),
                ('manage_card', models.CharField(max_length=13, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(unique=True)),
                ('edu', models.CharField(max_length=10, unique=True)),
                ('max_lend_count', models.IntegerField(default=0)),
                ('max_lend_day', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('book_name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=1)),
                ('book_add_datetime', models.DateTimeField(default=datetime.datetime(2023, 12, 21, 9, 11, 37, 519321, tzinfo=datetime.timezone.utc))),
                ('pubulisher', models.CharField(default='', max_length=200)),
                ('book_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_library.bookcategory')),
            ],
        ),
        migrations.CreateModel(
            name='IssuedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(default=datetime.date(2023, 12, 21))),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_library.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('card', models.CharField(default=None, max_length=50, unique=True)),
                ('specialty', models.CharField(max_length=50)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_library.education')),
            ],
        ),
        migrations.CreateModel(
            name='Lend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lend_date', models.DateTimeField(default=datetime.datetime(2023, 12, 21, 9, 11, 37, 522169, tzinfo=datetime.timezone.utc))),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_library.book')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_library.person')),
            ],
            options={
                'unique_together': {('person', 'book')},
            },
        ),
    ]
