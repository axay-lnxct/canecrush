# Generated by Django 3.2.25 on 2024-06-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cane_crush', '0002_auto_20240614_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
