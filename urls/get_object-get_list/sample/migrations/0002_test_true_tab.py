# Generated by Django 2.1 on 2018-09-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='true_tab',
            field=models.BooleanField(default=True),
        ),
    ]