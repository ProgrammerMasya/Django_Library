# Generated by Django 2.2.2 on 2019-06-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190626_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='updated_add',
            field=models.DateTimeField(null=True),
        ),
    ]