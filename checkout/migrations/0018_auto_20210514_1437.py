# Generated by Django 3.2.1 on 2021-05-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0017_auto_20210514_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase_history',
            name='card_exp',
        ),
        migrations.AddField(
            model_name='purchase_history',
            name='card_exp_month',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase_history',
            name='card_exp_year',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
