# Generated by Django 3.1.2 on 2021-12-20 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('birth_place', models.CharField(max_length=30)),
                ('birth_date', models.DateTimeField()),
                ('place', models.CharField(max_length=25)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Katholik', 'Katholik'), ('Protestan', 'Protestan'), ('Hindu', 'Hindu'), ('Buddha', 'Buddha')], max_length=25)),
            ],
        ),
    ]
