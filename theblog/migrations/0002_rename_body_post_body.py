# Generated by Django 4.0.4 on 2022-05-26 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='BODY',
            new_name='body',
        ),
    ]
