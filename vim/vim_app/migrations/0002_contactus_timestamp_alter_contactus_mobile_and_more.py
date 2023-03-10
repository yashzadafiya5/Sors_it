# Generated by Django 4.0.5 on 2023-02-21 06:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vim_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='mobile',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.TextField(max_length=120),
        ),
    ]
