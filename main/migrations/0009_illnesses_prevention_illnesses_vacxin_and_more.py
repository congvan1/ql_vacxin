# Generated by Django 4.0.4 on 2022-05-21 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_illnesses_description_alter_illnesses_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='illnesses',
            name='prevention',
            field=models.CharField(default=1, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='illnesses',
            name='vacxin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.vacxin'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Prevention',
        ),
    ]
