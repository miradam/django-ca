# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='cn',
            field=models.CharField(max_length=64, verbose_name='CommonName'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='csr',
            field=models.TextField(verbose_name='CSR'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='pub',
            field=models.TextField(verbose_name='Public key'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='revoked_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Revoked on'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='revoked_reason',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Reason for revokation'),
        ),
    ]
