# Generated by Django 4.0.3 on 2022-03-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whitneyapp', '0002_sermon_alter_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sermon',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]