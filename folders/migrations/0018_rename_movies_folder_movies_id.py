# Generated by Django 3.2.12 on 2023-02-08 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0017_auto_20230204_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='folder',
            old_name='movies',
            new_name='movies_id',
        ),
    ]
