# Generated by Django 3.2.9 on 2022-01-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_address_address_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_1',
            field=models.CharField(max_length=150),
        ),
    ]
