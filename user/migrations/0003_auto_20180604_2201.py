# Generated by Django 2.0.5 on 2018-06-04 14:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_common_member_star_star_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common_member_star',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.forum_post'),
        ),
        migrations.AlterField(
            model_name='common_member_star',
            name='spid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.forum_school_info'),
        ),
        migrations.AlterField(
            model_name='common_member_star',
            name='star_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 4, 22, 1, 20, 564632)),
        ),
    ]
