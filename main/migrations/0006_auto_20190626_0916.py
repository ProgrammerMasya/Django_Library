# Generated by Django 2.2.2 on 2019-06-26 09:16

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_book_pages_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_add',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 26, 9, 15, 46, 414967)),
        ),
        migrations.AddField(
            model_name='book',
            name='updated_add',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
