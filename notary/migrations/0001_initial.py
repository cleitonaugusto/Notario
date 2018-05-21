# Generated by Django 2.0.5 on 2018-05-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('file_mime_type', models.CharField(max_length=100)),
                ('file_size', models.IntegerField()),
                ('file_last_modified', models.DateField()),
                ('file_hash', models.CharField(max_length=66)),
                ('has_proof', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_digest', models.CharField(blank=True, db_index=True, max_length=100, verbose_name='secret_key')),
                ('timestamp_string', models.CharField(blank=True, db_index=True, max_length=20, verbose_name='secret_key')),
            ],
        ),
    ]
