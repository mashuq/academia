# Generated by Django 3.1.6 on 2021-06-14 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210614_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='contribution',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
