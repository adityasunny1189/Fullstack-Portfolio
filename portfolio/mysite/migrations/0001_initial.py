# Generated by Django 3.2.4 on 2021-06-21 21:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=20)),
                ('end_date', models.DateField(max_length=20, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('excerpt', models.TextField(max_length=200)),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(20)])),
                ('tags', models.ManyToManyField(to='mysite.Tag')),
            ],
        ),
    ]
