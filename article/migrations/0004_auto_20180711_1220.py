# Generated by Django 2.0.6 on 2018-07-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_articlepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=500),
        ),
    ]