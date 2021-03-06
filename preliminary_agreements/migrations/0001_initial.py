# Generated by Django 4.0.2 on 2022-03-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Preliminary_agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_agreement', models.DateField()),
                ('number_of_trip_members', models.IntegerField(max_length=11)),
                ('start_date_of_trip', models.DateField()),
                ('end_date_of_trip', models.DateField()),
            ],
            options={
                'db_table': 'preliminary_agreement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Visiting_city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'visiting_city',
                'managed': False,
            },
        ),
    ]
