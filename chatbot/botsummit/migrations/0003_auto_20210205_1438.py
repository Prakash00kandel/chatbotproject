# Generated by Django 3.1.3 on 2021-02-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botsummit', '0002_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='time',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='notes',
            field=models.CharField(default='hh', max_length=1000),
            preserve_default=False,
        ),
    ]
