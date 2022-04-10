# Generated by Django 3.0.7 on 2022-03-15 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('location', models.TextField(max_length=100)),
                ('more_info', models.TextField(max_length=100)),
                ('days', models.TextField(max_length=100)),
                ('month', models.TextField(max_length=100)),
                ('day_of_week', models.TextField(max_length=100)),
                ('dates_duration', models.TextField(max_length=100)),
            ],
        ),
    ]