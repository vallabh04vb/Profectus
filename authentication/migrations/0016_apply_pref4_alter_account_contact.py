# Generated by Django 4.2.1 on 2023-05-26 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_alter_account_id_alter_apply_id_alter_make_resume_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='pref4',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='account',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
