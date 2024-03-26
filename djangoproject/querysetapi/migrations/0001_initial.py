# Generated by Django 4.1.7 on 2023-04-24 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('eid', models.EmailField(max_length=254, unique=True)),
                ('eaddress', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
            ],
        ),
    ]
