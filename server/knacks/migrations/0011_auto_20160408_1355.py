# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('knacks', '0010_auto_20160403_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knack',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knacks.Category', verbose_name='Knack category'),
        ),
        migrations.AlterField(
            model_name='knack',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Tell us more about what you do'),
        ),
        migrations.AlterField(
            model_name='knack',
            name='how_charge',
            field=models.CharField(choices=[('Flat Fee', 'Flat Fee'), ('Hourly', 'Hourly')], default='Hourly', max_length=255, verbose_name='How do you charge?'),
        ),
        migrations.AlterField(
            model_name='knack',
            name='miles',
            field=models.CharField(choices=[('5 miles', '5 miles'), ('10 miles', '10 miles'), ('20 miles', '20 miles'), ('50+ miles', '50+ miles'), ('On Campus', 'On Campus')], default='On Campus', max_length=255, verbose_name='How many miles?'),
        ),
        migrations.AlterField(
            model_name='knack',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Knack headline'),
        ),
        migrations.AlterField(
            model_name='knack',
            name='photo0',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='knack',
            name='photo1',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='knack',
            name='photo2',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='knack',
            name='photo3',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='knack',
            name='photo4',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='knack',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='What is your rate?'),
        ),
        migrations.AlterField(
            model_name='knack',
            name='schedule',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="What's your schedule like?"),
        ),
        migrations.AlterField(
            model_name='knack',
            name='type',
            field=models.CharField(choices=[('O', 'Offered'), ('W', 'Wanted')], default='O', max_length=1),
        ),
        migrations.AlterField(
            model_name='knack',
            name='username',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Anonymous Username'),
        ),
        migrations.AlterField(
            model_name='knack',
            name='willing_to_travel',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Are you willing to travel?'),
        ),
        migrations.AlterField(
            model_name='knackidea',
            name='business_model',
            field=redactor.fields.RedactorField(default='', verbose_name='Business Model'),
        ),
        migrations.AlterField(
            model_name='knackidea',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knacks.Category', verbose_name='Knack category'),
        ),
        migrations.AlterField(
            model_name='knackidea',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Tell us more about what you do'),
        ),
        migrations.AlterField(
            model_name='knackidea',
            name='how_charge',
            field=models.CharField(choices=[('Flat Fee', 'Flat Fee'), ('Hourly', 'Hourly')], default='Hourly', max_length=255, verbose_name='How do you charge?'),
        ),
        migrations.AlterField(
            model_name='knackidea',
            name='miles',
            field=models.CharField(choices=[('5 miles', '5 miles'), ('10 miles', '10 miles'), ('20 miles', '20 miles'), ('50+ miles', '50+ miles'), ('On Campus', 'On Campus')], default='On Campus', max_length=255, verbose_name='How many miles?'),
        ),
        migrations.AlterField(
            model_name='knackidea',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Knack headline'),
        ),
        migrations.AlterField(
            model_name='knackidea',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='What is your rate?'),
        ),
        migrations.AlterField(
            model_name='knackidea',
            name='schedule',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="What's your schedule like?"),
        ),
        migrations.AlterField(
            model_name='knackidea',
            name='type',
            field=models.CharField(choices=[('O', 'Offered')], default='O', max_length=1),
        ),
        migrations.AlterField(
            model_name='knackidea',
            name='willing_to_travel',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Are you willing to travel?'),
        ),
        migrations.AlterField(
            model_name='knackideaimage',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='knacks/images/'),
        ),
    ]
