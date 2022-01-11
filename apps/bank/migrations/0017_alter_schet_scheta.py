# Generated by Django 4.0 on 2022-01-11 11:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0016_alter_schet_scheta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schet',
            name='scheta',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MaxLengthValidator(8), django.core.validators.MinLengthValidator(7)]),
        ),
    ]
