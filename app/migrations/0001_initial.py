# Generated by Django 2.0.2 on 2018-04-27 03:30

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
            name='employ',
            fields=[
                ('employ_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('employ_title', models.CharField(max_length=32)),
                ('employ_date', models.DateTimeField()),
                ('employ_owner', models.CharField(max_length=8)),
                ('employ_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='level',
            fields=[
                ('level_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('level_now', models.CharField(max_length=5)),
                ('level_credit', models.CharField(max_length=5)),
                ('level_money', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('task_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('task_title', models.CharField(max_length=32)),
                ('task_award', models.CharField(max_length=5)),
                ('task_date', models.DateTimeField(auto_now=True)),
                ('task_owner_id', models.CharField(max_length=8)),
                ('task_applyer_id', models.CharField(max_length=8, null=True)),
                ('task_info', models.TextField(null=True)),
                ('task_status_id', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='task_status',
            fields=[
                ('task_status_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('task_status_is_begin', models.CharField(max_length=1)),
                ('task_status_is_end', models.CharField(max_length=1)),
                ('task_status_is_apply', models.CharField(max_length=1)),
                ('task_status_is_agree', models.CharField(max_length=1)),
                ('task_status_publish_time', models.DateTimeField()),
                ('task_status_begin_time', models.DateTimeField()),
                ('task_status_finish_time', models.DateTimeField()),
                ('task_status_apply_time', models.DateTimeField()),
                ('task_status_agree_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=16)),
                ('user_password', models.CharField(max_length=16)),
                ('user_sex', models.CharField(choices=[(0, 'M'), (1, 'W'), (2, 'X')], default='X', max_length=1)),
                ('user_email', models.CharField(max_length=20, unique=True)),
                ('user_phone', models.CharField(max_length=11, unique=True)),
                ('user_regist_time', models.DateTimeField(auto_now=True)),
                ('user_level_id', models.CharField(max_length=8)),
                ('user_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
