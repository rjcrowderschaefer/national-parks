# Generated by Django 4.2.2 on 2023-07-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_state_parknum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=500)),
                ('parknum', models.CharField(default=0, max_length=10)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
