# Generated by Django 4.1.3 on 2022-11-23 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caregory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('point_five', models.DecimalField(decimal_places=2, max_digits=5)),
                ('one', models.DecimalField(decimal_places=2, max_digits=5)),
                ('one_point_five', models.DecimalField(decimal_places=2, max_digits=5)),
                ('two', models.DecimalField(decimal_places=2, max_digits=5)),
                ('twe_point_five', models.DecimalField(decimal_places=2, max_digits=5)),
                ('three', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bakery.caregory')),
            ],
        ),
    ]
