# Generated by Django 2.2 on 2020-06-05 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200605_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
