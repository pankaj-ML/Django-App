# Generated by Django 3.2.7 on 2021-09-19 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='desc',
        ),
    ]
