# Generated by Django 4.1.5 on 2023-04-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('recipe', models.URLField()),
                ('ingres', models.JSONField(default=' ')),
                ('instruct', models.JSONField(default=' ')),
            ],
        ),
    ]