# Generated by Django 4.1.7 on 2023-04-20 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelinheritance', '0002_bank_bankmanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('ulocation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('modelinheritance.university',),
        ),
    ]