# Generated by Django 3.0.5 on 2020-05-17 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_auto_20200515_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=150, verbose_name='Имя треда')),
                ('post_content', models.TextField(max_length=15000, verbose_name='Тело треда')),
                ('post_date', models.DateField(default=datetime.date.today, verbose_name='Дата создания')),
                ('url', models.SlugField(max_length=160)),
            ],
            options={
                'verbose_name': 'Тред',
                'verbose_name_plural': 'Треды',
            },
        ),
    ]