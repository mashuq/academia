# Generated by Django 3.1.6 on 2021-03-30 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_testimonial_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
