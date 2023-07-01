# Generated by Django 4.2.2 on 2023-07-01 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceTerritory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('placetype', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('territory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='territoryplaces', to='main_app.territory')),
            ],
        ),
    ]