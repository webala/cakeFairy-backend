# Generated by Django 4.1.3 on 2022-11-23 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0004_alter_flavour_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='flavour',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
