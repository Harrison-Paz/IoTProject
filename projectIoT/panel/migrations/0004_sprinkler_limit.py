# Generated by Django 4.1.4 on 2023-01-12 23:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_alter_sprinkler_codsprinkler'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprinkler',
            name='limit',
            field=models.IntegerField(default=80, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]