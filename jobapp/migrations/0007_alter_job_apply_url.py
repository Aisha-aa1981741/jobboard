# Generated by Django 4.2.2 on 2023-06-14 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_job_apply_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='apply_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
