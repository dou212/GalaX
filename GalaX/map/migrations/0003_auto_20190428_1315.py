# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 13:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20190324_2238'),
        ('map', '0002_auto_20190417_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '喜欢',
                'verbose_name_plural': '喜欢',
                'ordering': ['-c_time'],
            },
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-c_time'], 'verbose_name': '事件', 'verbose_name_plural': '事件'},
        ),
        migrations.AddField(
            model_name='event',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 4, 28, 13, 15, 1, 196781)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='repost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='map.Event'),
        ),
        migrations.AddField(
            model_name='like',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='map.Event'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='map.Event'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
    ]