# Generated by Django 3.2.23 on 2024-01-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
