# Generated by Django 3.0.5 on 2020-05-25 13:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_auto_20200525_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainpage.Comment', verbose_name='Родитель комментарий'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 25, 13, 13, 13, 603950, tzinfo=utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='tred_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Tred', verbose_name='Родитель тред'),
        ),
        migrations.AlterField(
            model_name='tred',
            name='tred_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 13, 13, 13, 602952, tzinfo=utc), verbose_name='Дата создания'),
        ),
    ]