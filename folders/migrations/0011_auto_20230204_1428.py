# Generated by Django 3.2.12 on 2023-02-04 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_poster'),
        ('folders', '0010_auto_20230204_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='movies',
        ),
        migrations.AddField(
            model_name='folder',
            name='movies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
    ]