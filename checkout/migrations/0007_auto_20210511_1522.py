# Generated by Django 3.2.1 on 2021-05-11 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_info', '0002_item_type_image'),
        ('checkout', '0006_auto_20210511_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='cardHolder',
            field=models.CharField(default='Jane', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cards',
            name='cardNumber',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cards',
            name='expiryDate',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkout',
            name='items',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product_info.items'),
            preserve_default=False,
        ),
    ]
