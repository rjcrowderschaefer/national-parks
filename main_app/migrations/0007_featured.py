# Generated by Django 4.2.2 on 2023-07-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_place_image_placeterritory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('places', models.ManyToManyField(to='main_app.place')),
            ],
        ),
    ]
