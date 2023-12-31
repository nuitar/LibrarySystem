# Generated by Django 5.0 on 2023-12-21 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_library', '0008_rename_pubulisher_book_publisher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_add_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 21, 12, 45, 32, 918847, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lend',
            name='lend_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 21, 12, 45, 32, 921691, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='reserve_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 21, 12, 45, 32, 922502, tzinfo=datetime.timezone.utc)),
        ),
    ]
