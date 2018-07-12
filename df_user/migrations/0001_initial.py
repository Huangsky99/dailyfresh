# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ashou', models.CharField(max_length=50)),
                ('aadd', models.CharField(max_length=100)),
                ('aphone', models.CharField(max_length=11)),
                ('ayoubian', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=32)),
                ('uemail', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='addressinfo',
            name='auser',
            field=models.ForeignKey(to='df_user.UserInfo'),
        ),
    ]
