# Generated by Django 3.2.16 on 2022-11-03 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yelpuser',
            name='yelping_since',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
