# Generated by Django 3.2.9 on 2021-12-04 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_size_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_table',
            name='size_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.size_type', to_field='size_types'),
        ),
    ]
