# Generated by Django 3.2.1 on 2021-05-14 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0019_auto_20210514_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_history',
            name='card_cvc',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='purchase_history',
            name='card_exp_month',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='purchase_history',
            name='card_exp_year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='purchase_history',
            name='card_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(16)]),
        ),
    ]
