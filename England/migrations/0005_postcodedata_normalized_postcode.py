# Generated by Django 5.0.6 on 2024-09-15 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('England', '0004_alter_postcodedata_postcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcodedata',
            name='normalized_postcode',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
    ]
