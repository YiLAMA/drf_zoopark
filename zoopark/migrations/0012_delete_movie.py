# Generated by Django 3.0.8 on 2020-11-01 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoopark', '0011_remove_movie_poster'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie',
        ),
    ]