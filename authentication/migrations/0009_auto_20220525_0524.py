# Generated by Django 3.0 on 2022-05-25 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20220524_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='pdf',
            new_name='Resume',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='author',
        ),
    ]
