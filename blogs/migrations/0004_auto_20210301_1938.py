# Generated by Django 3.1.3 on 2021-03-01 14:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20210210_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='background',
            field=models.ImageField(blank=True, upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_3',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='image1',
            field=models.ImageField(default='', upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image2',
            field=models.ImageField(default='', upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='blog',
            name='quote',
            field=models.CharField(blank=True, default='', max_length=2000000000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, default='', max_length=2000000000),
        ),
    ]
