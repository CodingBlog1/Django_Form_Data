# Generated by Django 4.2.3 on 2023-07-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField()),
                ('mname', models.CharField(max_length=70)),
                ('memail', models.EmailField(max_length=70)),
                ('mnumber', models.BigIntegerField()),
            ],
        ),
    ]
