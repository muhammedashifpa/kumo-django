# Generated by Django 3.2.9 on 2021-12-04 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_types', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.size_type', to_field='size_types')),
            ],
        ),
        migrations.CreateModel(
            name='Product_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('category', models.CharField(choices=[('Shirt', 'Shirt'), ('T Shirt', 'T Shirt'), ('Sport Wear', 'Sport Wear'), ('Out Wear', 'Out Wear'), ('Jackets', 'Jackets'), ('Trousers and shorts', 'Trousers and shorts'), ('Jeans', 'Jeans'), ('Jumpsuit', 'Jumpsuit'), ('Sweatshirt', 'Sweatshirt'), ('Jeans', 'Jeans')], max_length=20)),
                ('gender', models.CharField(choices=[('MEN', 'MEN'), ('WOMEN', 'WOMEN'), ('KIDS', 'KIDS'), ('UNISEX', 'UNISEX')], max_length=20)),
                ('price', models.IntegerField()),
                ('offer_price', models.FloatField(null=True)),
                ('offer_percentage', models.FloatField(null=True)),
                ('stock', models.IntegerField()),
                ('description', models.TextField(default='', max_length=500)),
                ('size_type', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='prd_img')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='prd_img')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='prd_img')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='prd_img')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand', to_field='brand')),
            ],
        ),
    ]
