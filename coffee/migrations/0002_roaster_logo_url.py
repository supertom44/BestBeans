# Generated by Django 2.0.7 on 2018-07-21 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roaster',
            name='logo_url',
            field=models.URLField(null=True),
        ),
    ]
