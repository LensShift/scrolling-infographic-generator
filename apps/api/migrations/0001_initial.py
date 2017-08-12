# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Infographic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('status', models.CharField(choices=[('d', 'Draft'), ('r', 'Ready')], max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('background_video', models.FileField(blank=True, null=True, upload_to='videos')),
                ('background_image', models.FileField(blank=True, null=True, upload_to='images')),
                ('text', models.TextField()),
                ('text_position_x', models.IntegerField(default=0)),
                ('text_position_y', models.IntegerField(default=0)),
                ('section_position', models.PositiveSmallIntegerField()),
                ('infographic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Infographic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]