from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
from django.contrib.auth.models import User
from mimesis import Person
from blog.models import Post, Comment, Vote, Favorite
from django.core.files import File
import random
from faker import Faker
# import csv

def get_path(file):
    return os.path.join(settings.BASE_DIR, 'blog/management/commands/imports/', file)

class Command(BaseCommand):
    help = "Create fake data for testing blog layout"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Deleting database!')
        Post.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()
        Comment.objects.all().delete()
        Favorite.objects.all().delete()
        Like.objects.all().delete()

        fake = Faker()
        # populator = Faker.getPopulator()

        users = []
        for fake_user in range(51):
            fake_user = User.objects.create_user(slugify(fake.name()), fake.email(), 'password')
            users.append(fake_user)
        print("50 Fake users created!")

        fake_posts = []
        for i in range(51):
            post_dictionary = {
                'title': fake.sentence(),
                'description': fake.text(),
                'user': users[random.randrange(0, 50)],
            }
            fake_posts.append(post_dictionary)

        posts = []
        for post_data in fake_posts:
            post = Post.objects.create(**post_data)
            posts.append(post)
        print('50 Posts imported!!!')

        for i in range(50):
            Like.objects.create(post=posts[random.randrange(0, 50)], user=users[i])
        print('50 Likes imported!!!')

        for i in range(50):
            Favorite.objects.create(post=posts[random.randrange(0, 50)], user=users[i])
        print('50 Favorites imported!!!')

        for i in range(101):
            Comment.objects.create(post=posts[random.randrange(0, 50)], user=users[random.randrange(0, 50)])
        print('100 comments imported!')

        print('All data imported successfully!')
