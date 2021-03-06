# Generated by Django 3.2.1 on 2021-05-14 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0020_auto_20210514_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_history',
            name='card_cvc',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='purchase_history',
            name='card_exp_month',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='purchase_history',
            name='card_exp_year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='purchase_history',
            name='card_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000000000000000), django.core.validators.MaxValueValidator(9999999999999999)]),
        ),
    ]
