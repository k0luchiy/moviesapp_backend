# Generated by Django 3.2.12 on 2023-02-04 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20230204_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='movies_interaction',
        ),
        migrations.DeleteModel(
            name='MovieInteraction',
        ),
    ]
