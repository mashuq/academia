# Generated by Django 3.1.6 on 2021-02-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_notelesson_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiolesson',
            name='link',
        ),
        migrations.AddField(
            model_name='audiolesson',
            name='embed',
            field=models.TextField(default='abc'),
            preserve_default=False,
        ),
    ]