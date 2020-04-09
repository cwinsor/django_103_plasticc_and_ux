# Generated by Django 3.0.3 on 2020-04-05 22:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gameplay', '0002_plasticcstar_foo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='foo',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]