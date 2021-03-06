# Generated by Django 3.2.1 on 2021-05-10 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('price', models.FloatField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_info.item_type')),
            ],
        ),
        migrations.CreateModel(
            name='Items_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.CharField(max_length=255)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_info.items')),
            ],
        ),
        migrations.CreateModel(
            name='Item_Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_info.items')),
            ],
        ),
    ]
