# Generated by Django 3.0.5 on 2020-04-07 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200407_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]