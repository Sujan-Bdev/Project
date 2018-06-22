# Generated by Django 2.0.1 on 2018-06-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20180621_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Book Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='title'),
        ),
    ]