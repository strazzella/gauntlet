# Generated by Django 4.0.3 on 2022-03-06 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20171204_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='last_accessed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]