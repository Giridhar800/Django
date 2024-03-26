# Generated by Django 4.1.7 on 2023-04-20 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelinheritance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=20)),
                ('baddress', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BankManager',
            fields=[
                ('bank_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelinheritance.bank')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
            bases=('modelinheritance.bank',),
        ),
    ]