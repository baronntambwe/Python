# Generated by Django 2.2.5 on 2020-02-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=24)),
                ('lastName', models.CharField(max_length=24)),
                ('email', models.EmailField(max_length=24, unique=True)),
            ],
        ),
    ]
