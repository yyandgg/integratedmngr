# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sysid', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('functionregid', models.IntegerField(null=True, blank=True)),
                ('grade', models.IntegerField()),
                ('ordeno', models.BooleanField()),
                ('parentid', models.IntegerField()),
                ('url', models.CharField(max_length=200, null=True, blank=True)),
                ('icon', models.CharField(max_length=200, null=True, blank=True)),
                ('parameter', models.CharField(max_length=200, null=True, blank=True)),
                ('createtime', models.DateField(auto_now=True)),
                ('updatetine', models.DateField(auto_now_add=True)),
                ('isonlycenter', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'yes'), (b'2', b'no')])),
            ],
        ),
        migrations.CreateModel(
            name='Menupermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roleid', models.BigIntegerField()),
                ('meunid', models.BigIntegerField()),
                ('orgid', models.IntegerField()),
                ('create_time', models.DateField(auto_now=True)),
                ('update_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('describes', models.CharField(max_length=100, null=True, blank=True)),
                ('createtime', models.DateField(auto_now=True)),
                ('updatetime', models.DateField(auto_now_add=True)),
                ('orgid_display', models.CharField(max_length=225, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30, null=True, blank=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10, null=True, blank=True)),
                ('idcard', models.CharField(max_length=10, null=True, blank=True)),
                ('password', models.CharField(max_length=200)),
                ('status', models.CharField(default=1, max_length=1, choices=[(b'1', b'normal'), (b'2', b'suoding'), (b'3', b'colod'), (b'4', b'cancel')])),
                ('createtime', models.DateField(auto_now=True)),
                ('updatetime', models.DateField(auto_now_add=True)),
                ('isfirstlogin', models.IntegerField(null=True, blank=True)),
                ('updatepassword', models.DateField(auto_now_add=True)),
                ('freezedate', models.DateField(null=True, blank=True)),
                ('lastlogin', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
