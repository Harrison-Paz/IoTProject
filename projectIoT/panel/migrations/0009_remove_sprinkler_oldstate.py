# Generated by Django 4.1.4 on 2023-01-13 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0008_sprinkler_oldstate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprinkler',
            name='oldState',
        ),
    ]