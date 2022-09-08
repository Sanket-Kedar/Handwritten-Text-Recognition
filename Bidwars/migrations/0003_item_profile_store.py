# Generated by Django 3.2.4 on 2021-09-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bidwars', '0002_alter_register_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('total_item', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('hobby', models.CharField(max_length=50)),
                ('income', models.CharField(max_length=100)),
                ('except_amount', models.IntegerField(null=True)),
                ('age', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=100)),
                ('email', models.CharField(default=' ', max_length=100)),
                ('phone', models.CharField(default=' ', max_length=10)),
                ('address', models.TextField()),
                ('country', models.CharField(default=' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('in_stock', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image1', models.ImageField(null=True, upload_to='store/')),
                ('image2', models.ImageField(null=True, upload_to='store/')),
                ('image3', models.ImageField(null=True, upload_to='store/')),
                ('condition', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
