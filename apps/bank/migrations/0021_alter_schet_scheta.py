# Generated by Django 4.0 on 2022-01-11 12:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0020_alter_schet_scheta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schet',
            name='scheta',
            field=models.DecimalField(decimal_places=0, max_digits=8, validators=[django.core.validators.DecimalValidator(decimal_places=0, max_digits=5)]),
        ),
    ]
