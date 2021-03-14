# Generated by Django 2.2.10 on 2021-03-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authorize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fun_name', models.CharField(max_length=50, null=True)),
                ('parent_name', models.CharField(max_length=50, null=True)),
                ('fun_group', models.CharField(max_length=50, null=True)),
                ('fun_url', models.CharField(max_length=50, null=True)),
                ('img_url', models.CharField(max_length=50, null=True)),
                ('status', models.SmallIntegerField(null=True)),
                ('creator', models.CharField(max_length=100, null=True)),
                ('create_time', models.DateTimeField(null=True)),
                ('update_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'cfg_sys_authorize',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50, null=True)),
                ('parent_name', models.CharField(max_length=50, null=True)),
                ('area', models.CharField(max_length=50, null=True)),
                ('status', models.SmallIntegerField(null=True)),
                ('creator', models.CharField(max_length=100, null=True)),
                ('create_time', models.DateTimeField(null=True)),
                ('update_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'cfg_sys_department',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('username', models.CharField(max_length=100)),
                ('log_type', models.IntegerField(null=True)),
                ('from_ip', models.CharField(max_length=100, null=True)),
                ('feature', models.CharField(max_length=100, null=True)),
                ('sub_feature', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(null=True)),
                ('log_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'cfg_sys_log',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('use_authorize', models.TextField(null=True)),
                ('data_authorize', models.TextField(null=True)),
                ('data_create_authorize', models.TextField(null=True)),
                ('status', models.SmallIntegerField(null=True)),
                ('creator', models.CharField(max_length=100, null=True)),
                ('create_time', models.DateTimeField(null=True)),
                ('update_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'cfg_sys_role',
            },
        ),
        migrations.CreateModel(
            name='StreetArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('county', models.CharField(max_length=200, null=True)),
                ('street', models.CharField(max_length=200, null=True)),
                ('other_flag', models.CharField(max_length=200, null=True)),
                ('lng', models.CharField(max_length=50, null=True)),
                ('lat', models.CharField(max_length=50, null=True)),
                ('bd_lng', models.CharField(max_length=50, null=True)),
                ('bd_lat', models.CharField(max_length=50, null=True)),
                ('remark', models.CharField(max_length=200, null=True)),
                ('update_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'cfg_sys_area',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100, null=True)),
                ('user_name', models.CharField(max_length=50, null=True)),
                ('user_pwd', models.CharField(max_length=50, null=True)),
                ('real_name', models.CharField(max_length=50, null=True)),
                ('msisdn', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('img_path', models.CharField(max_length=100, null=True)),
                ('role_id', models.IntegerField(null=True)),
                ('department_id', models.IntegerField(null=True)),
                ('status', models.SmallIntegerField(null=True)),
                ('creator', models.CharField(max_length=100, null=True)),
                ('create_time', models.DateTimeField(null=True)),
                ('update_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'cfg_sys_user',
            },
        ),
        migrations.CreateModel(
            name='VersionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_code', models.CharField(max_length=100, null=True)),
                ('varsion_name', models.CharField(max_length=100, null=True)),
                ('app_version_code', models.IntegerField(null=True)),
                ('app_version', models.CharField(max_length=100, null=True)),
                ('app_version_name', models.CharField(max_length=100, null=True)),
                ('update_summary', models.CharField(max_length=500, null=True)),
                ('update_info', models.TextField(null=True)),
                ('app_down_addr', models.CharField(max_length=200, null=True)),
                ('is_force_udapte', models.IntegerField(null=True)),
                ('create_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'cfg_sys_version_info',
            },
        ),
    ]
