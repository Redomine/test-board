# Generated by Django 3.0.5 on 2020-05-22 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0014_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
    ]
