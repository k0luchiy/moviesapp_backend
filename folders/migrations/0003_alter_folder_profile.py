# Generated by Django 3.2.12 on 2023-02-04 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('folders', '0002_folder_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folders', to='profiles.profile'),
        ),
    ]
