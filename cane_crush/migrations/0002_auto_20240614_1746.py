# Generated by Django 3.2.25 on 2024-06-14 12:16

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cane_crush', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='currency',
        ),
        migrations.AlterField(
            model_name='country',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
