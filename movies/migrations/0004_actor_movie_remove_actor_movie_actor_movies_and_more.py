# Generated by Django 4.0.2 on 2022-02-16 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_actor_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor_Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'actors_movies',
            },
        ),
        migrations.RemoveField(
            model_name='actor',
            name='movie',
        ),
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(related_name='actors', through='movies.Actor_Movie', to='movies.Movie'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='actor',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='actor_movie',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.actor'),
        ),
        migrations.AddField(
            model_name='actor_movie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
    ]
