# Generated by Django 3.2.1 on 2021-05-11 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20210511_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase_history',
            name='card',
        ),
        migrations.DeleteModel(
            name='Cards',
        ),
    ]