# Generated by Django 4.1.5 on 2023-02-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.URLField(default=' '),
            preserve_default=False,
        ),
    ]
