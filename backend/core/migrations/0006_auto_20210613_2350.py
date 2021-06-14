# Generated by Django 3.1.6 on 2021-06-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_session_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
