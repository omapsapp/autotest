# Generated by Django 2.2.2 on 2019-07-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('falcon',
         '0002_auto_20190709_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildSessions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('build_number', models.IntegerField(blank=True, null=True)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('caused_by', models.CharField(blank=True, max_length=100, null=True)),
                ('upstream_job', models.CharField(blank=True, max_length=100, null=True)),
                ('upstream_build_number', models.CharField(blank=True, max_length=10, null=True)),
                ('upstream_url', models.CharField(blank=True, max_length=250, null=True)),
                ('jenkins_job', models.CharField(blank=True, max_length=250, null=True)),
                ('release', models.CharField(blank=True, max_length=20, null=True)),
                ('release_type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'build_sessions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('device_id', models.CharField(max_length=50)),
                ('udid', models.CharField(blank=True, max_length=100, null=True)),
                ('platform_name', models.CharField(blank=True, max_length=20, null=True)),
                ('platform_version', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('battery_level', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'devices',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemoryMetricsRaw',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('record_timestamp', models.DateTimeField()),
                ('total_memory_in_bytes', models.IntegerField()),
            ],
            options={
                'db_table': 'memory_metrics_raw',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemoryMetricsStandart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('record_timestamp', models.DateTimeField()),
                ('total_memory_in_bytes', models.IntegerField()),
            ],
            options={
                'db_table': 'memory_metrics_standart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MonkeyCrashes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('crash_number', models.IntegerField(blank=True, null=True)),
                ('crash_text', models.CharField(blank=True, max_length=3000, null=True)),
            ],
            options={
                'db_table': 'monkey_crashes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PowerMetricsRaw',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('current', models.FloatField()),
                ('voltage', models.FloatField()),
                ('power', models.FloatField()),
                ('charge', models.FloatField()),
                ('energy', models.FloatField()),
                ('record_timestamp', models.DateTimeField()),
            ],
            options={
                'db_table': 'power_metrics_raw',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PowerMetricsStandart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('current', models.FloatField()),
                ('voltage', models.FloatField()),
                ('power', models.FloatField()),
                ('charge', models.FloatField()),
                ('energy', models.FloatField()),
                ('record_timestamp', models.DateTimeField()),
            ],
            options={
                'db_table': 'power_metrics_standart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReleaseFeatures',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('requirements_status', models.CharField(blank=True, max_length=50, null=True)),
                ('dev_status', models.CharField(blank=True, max_length=50, null=True)),
                ('testing_status', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'release_features',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Releases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('create_time', models.DateTimeField(null=True)),
                ('time_start', models.DateTimeField(blank=True, null=True)),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('is_archive', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'releases',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('method_name', models.CharField(blank=True, max_length=250, null=True)),
                ('comment', models.CharField(blank=True, max_length=1500, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'test_items',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestResults',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('is_memory_test', models.BooleanField(blank=True, null=True)),
                ('is_power_test', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'test_results',
                'managed': False,
            },
        ),

        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('hotel_id', models.IntegerField(blank=True, null=True)),
                ('aid', models.IntegerField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=1000, null=True)),
                ('booking_time', models.DateTimeField(blank=True, null=True)),
                ('reservation_id', models.CharField(blank=True, max_length=20, null=True)),
                ('test_result', models.ForeignKey('TestResults', models.CASCADE, blank=True, null=True))
            ],
            options={
                'db_table': 'bookings',
            },
        ),
    ]
