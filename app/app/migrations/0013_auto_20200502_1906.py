# Generated by Django 2.2.12 on 2020-05-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200502_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='projectvendorassign',
            name='project_id',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
