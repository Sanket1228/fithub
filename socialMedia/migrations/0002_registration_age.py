# Generated by Django 3.1.2 on 2021-03-17 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialMedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
