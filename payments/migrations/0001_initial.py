# Generated by Django 4.0.2 on 2022-03-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('rate', models.IntegerField()),
            ],
            options={
                'db_table': 'currency',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('organization', models.IntegerField()),
                ('amount_in_rubles', models.IntegerField()),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
    ]