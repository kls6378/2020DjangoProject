# Generated by Django 2.2 on 2020-06-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='Asia/Seoul'),
            preserve_default=False,
        ),
    ]
