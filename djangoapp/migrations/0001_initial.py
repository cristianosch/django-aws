# Generated by Django 4.2.5 on 2023-09-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('user', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(max_length=400, null=True)),
            ],
        ),
    ]
