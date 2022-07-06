# Generated by Django 4.0.5 on 2022-07-06 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=80)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]