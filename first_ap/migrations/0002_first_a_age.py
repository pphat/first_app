# Generated by Django 3.0 on 2019-12-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_ap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='first_a',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
