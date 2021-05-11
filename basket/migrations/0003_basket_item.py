# Generated by Django 3.2.1 on 2021-05-11 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_info', '0002_item_type_image'),
        ('basket', '0002_alter_basket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product_info.items'),
            preserve_default=False,
        ),
    ]