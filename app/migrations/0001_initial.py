# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 11:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('date_added', models.DateTimeField(auto_now=True, verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=256, verbose_name='State')),
                ('city', models.CharField(max_length=256, verbose_name='City')),
                ('closest_bstop', models.CharField(max_length=256, verbose_name='Closest Bustop')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now=True, verbose_name='date added')),
                ('extra_details', models.TextField(verbose_name='extra details')),
                ('total_amount', models.CharField(max_length=250, verbose_name='total amount')),
                ('invoice_number', models.CharField(max_length=250, unique=True, verbose_name='invoice number')),
                ('tracking', models.CharField(choices=[('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Canceled', 'Canceled'), ('Complete', 'Complete'), ('Confirmed', 'Confirmed'), ('Denied', 'Denied'), ('Canceled Reversal', 'Canceled Reversal'), ('Failed', 'Failed'), ('Refunded', 'Refunded'), ('Reversed', 'Reversed'), ('Chargeback', 'Chargeback'), ('Pending', 'Pending'), ('Voided', 'Voided'), ('Processed', 'Processed'), ('Expired', 'Expired')], max_length=250, verbose_name='tracking')),
                ('payment_method', models.CharField(choices=[('Card', 'Card'), ('Pay On Delivery', 'Pay On Delivery'), ('Bank Deposit', 'Bank Deposit'), ('Bank Transfer', 'Bank Transfer')], max_length=250, verbose_name='payment method')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Location')),
                ('items', models.ManyToManyField(to='app.Item')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_of_order', to='app.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Product name')),
                ('sku', models.CharField(max_length=256, verbose_name='Stock keeping unit')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('date_added', models.DateTimeField(auto_now=True, verbose_name='Date added')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone number')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Location')),
                ('products', models.ManyToManyField(null=True, to='app.Product')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
    ]