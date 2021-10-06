# Generated by Django 2.2.12 on 2021-09-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('score', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
