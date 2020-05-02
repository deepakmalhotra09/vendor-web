# Generated by Django 2.2.12 on 2020-05-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0010_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('client_id', models.CharField(max_length=10)),
                ('link', models.CharField(max_length=150)),
                ('target', models.CharField(max_length=20)),
                ('cost', models.CharField(max_length=15)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]