# Generated by Django 5.2.2 on 2025-06-08 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreationEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=255)),
                ('features', models.TextField()),
                ('output', models.CharField(max_length=255)),
                ('objective', models.TextField()),
                ('dataset_type', models.CharField(choices=[('regresi', 'Regresi'), ('klasifikasi', 'Klasifikasi'), ('forecasting', 'Forecasting')], max_length=50)),
                ('training_status', models.CharField(choices=[('belum', 'Belum Dilatih'), ('proses', 'Proses'), ('sudah', 'Sudah Dilatih')], max_length=50)),
                ('accuracy', models.CharField(blank=True, max_length=50, null=True)),
                ('refining_strategy', models.CharField(blank=True, max_length=255, null=True)),
                ('refining_status', models.CharField(choices=[('belum', 'Belum'), ('proses', 'Proses'), ('sudah', 'Sudah')], max_length=50)),
                ('data_activity', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('upload_csv', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
