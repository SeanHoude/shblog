# Generated by Django 2.1.3 on 2018-11-29 01:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_remove_comment_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorite_posts', through='blog.Favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='upvoted',
            field=models.ManyToManyField(related_name='voted', through='blog.Vote', to=settings.AUTH_USER_MODEL),
        ),
    ]