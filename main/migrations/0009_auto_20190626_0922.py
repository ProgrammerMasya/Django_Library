# Generated by Django 2.2.2 on 2019-06-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190626_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='updated_add',
            field=models.DateTimeField(),
        ),
    ]