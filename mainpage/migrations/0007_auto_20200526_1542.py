# Generated by Django 3.0.5 on 2020-05-26 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_auto_20200526_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='tred',
            name='tred_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]
