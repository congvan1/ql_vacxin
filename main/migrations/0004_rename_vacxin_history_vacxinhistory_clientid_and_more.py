# Generated by Django 4.0.4 on 2022-05-21 02:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_vacxin_history_vacxinhistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacxinhistory',
            old_name='vacxin_history',
            new_name='clientID',
        ),
        migrations.RenameField(
            model_name='vacxinhistory',
            old_name='vacxin',
            new_name='vacxinID',
        ),
        migrations.AlterField(
            model_name='vacxinhistory',
            name='inject_next_time',
            field=models.DateField(default=datetime.date(2022, 6, 21)),
        ),
    ]
