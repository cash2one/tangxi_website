# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('date', models.DateField(auto_now_add=True, verbose_name='\u65e5\u671f')),
                ('description', models.CharField(max_length=5000, verbose_name='\u65b0\u95fb\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u4f01\u4e1a\u65b0\u95fb',
                'verbose_name_plural': '\u4f01\u4e1a\u65b0\u95fb',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u59d3\u540d')),
                ('gender', models.IntegerField(verbose_name='\u6027\u522b')),
                ('thumbnail', models.FileField(upload_to=b'employee_thumbnails/', verbose_name='\u7167\u7247')),
            ],
            options={
                'verbose_name': '\u5458\u5de5',
                'verbose_name_plural': '\u5458\u5de5',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('date', models.DateField(auto_now_add=True, verbose_name='\u65e5\u671f')),
                ('path', models.FileField(upload_to=b'share/', verbose_name='\u56fe\u7247\u8def\u5f84')),
            ],
            options={
                'verbose_name': '\u56fe\u7247',
                'verbose_name_plural': '\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u804c\u4f4d\u540d\u79f0')),
                ('date', models.DateField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65e5\u671f')),
                ('quantity', models.IntegerField(verbose_name='\u62db\u8058\u6570\u91cf')),
                ('description', models.TextField(verbose_name='\u804c\u4f4d\u62db\u8058\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u5de5\u4f5c\u673a\u4f1a',
                'verbose_name_plural': '\u5de5\u4f5c\u673a\u4f1a',
            },
        ),
        migrations.CreateModel(
            name='ServiceProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u670d\u52a1\u540d\u79f0')),
                ('image_title', models.CharField(max_length=100, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('description', models.TextField(verbose_name='\u670d\u52a1\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u57fa\u672c\u4fe1\u606f',
                'verbose_name_plural': '\u670d\u52a1\u57fa\u672c\u4fe1\u606f',
            },
        ),
    ]
