# Generated by Django 3.0.7 on 2020-07-04 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200704_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='creator',
            new_name='user',
        ),
    ]
