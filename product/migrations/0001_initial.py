# Generated by Django 3.1 on 2020-08-06 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('discount', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
