# Generated by Django 2.2.2 on 2019-06-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_book_amazon_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='amazon_rating',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
    ]
