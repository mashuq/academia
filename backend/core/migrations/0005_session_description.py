# Generated by Django 3.1.6 on 2021-06-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_linklesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
