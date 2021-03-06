# Generated by Django 2.1.1 on 2018-09-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20180925_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='profiles.Flight')),
            ],
        ),
    ]
