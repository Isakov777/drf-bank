# Generated by Django 4.0 on 2022-01-02 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_alter_schet_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]