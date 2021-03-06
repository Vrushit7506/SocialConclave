# Generated by Django 3.1.3 on 2021-02-10 09:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('title', models.CharField(blank=True, max_length=2000000000)),
                ('slug', models.CharField(blank=True, max_length=2000000000)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
