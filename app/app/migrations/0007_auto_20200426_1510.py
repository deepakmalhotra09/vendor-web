# Generated by Django 2.2.12 on 2020-04-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0006_auto_20200426_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='mobile_no',
            field=models.CharField(max_length=12),
        ),
    ]
