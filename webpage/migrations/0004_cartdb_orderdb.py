# Generated by Django 5.1.3 on 2025-01-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_userdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('ProductName', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('TotalPrice', models.IntegerField(blank=True, null=True)),
                ('Prod_Image', models.ImageField(blank=True, null=True, upload_to='Cart Images')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pin', models.IntegerField(blank=True, null=True)),
                ('total_price', models.IntegerField(blank=True, null=True)),
                ('message', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
