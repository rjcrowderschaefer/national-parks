# Generated by Django 4.2.2 on 2023-07-05 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featured',
            name='name',
        ),
    ]
