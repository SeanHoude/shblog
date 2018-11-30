from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
from django.contrib.auth.models import User
from mimesis import Person
from blog.models import Post, Comment, Vote, Favorite
from django.core.files import File
from django.template.defaultfilters import slugify
import csv
import random
from django_faker import Faker

def get_path(file):
    return os.path.join(settings.BASE_DIR, 'blog/management/commands/imports/', file)

class Command(BaseCommand):
    help = "Import books from books.csv"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Deleting database!')
        Post.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()
        Comment.objects.all().delete()
        Favorite.objects.all().delete()
        Vote.objects.all().delete()

        populator = Faker.getPopulator()

        

        users = []
        person = Person()
        for fake_user in range(50):
            fake_user = User.objects.create_user(person.username(), person.email(), 'password')
            users.append(fake_user)
        print("50 Fake users created!")

        fake_posts = [
            {
                'title': 'First Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('First Post')
            },
            {
                'title': 'Second Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Second Post')
            },
            {
                'title': 'Third Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Third Post')
            },
            {
                'title': 'Fourth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Fourth Post')
            },
            {
                'title': 'Fifth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Fifth Post')
            },
            {
                'title': 'Sixth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Sixth Post')
            },
            {
                'title': 'Seventh Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Seventh Post')
            },
            {
                'title': 'Eighth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Eighth Post')
            },
            {
                'title': 'Ninth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Ninth Post')
            },
            {
                'title': 'Tenth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Tenth Post')
            },
            {
                'title': 'Eleventh Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Eleventh Post')
            },
            {
                'title': 'Twelfth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Twelfth Post')
            },
            {
                'title': 'Thirteenth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Thirteenth Post')
            },
            {
                'title': 'Fourteenth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Fourteenth Post')
            },
            {
                'title': 'Fifteenth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Fifteenth Post')
            },
            {
                'title': 'Sixteenth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Sixteenth Post')
            },
            {
                'title': 'Seventeenth Post',
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'slug': slugify('Seventeenth Post')
            },
        ]

        fake_postsss = []
        for i in range(50):
            dict = {
                'title': f"This is example post{i}",
                'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, quod. Officiis vel, voluptatibus aliquid necessitatibus dolorum delectus? Deleniti veritatis atque rem odit ut, laudantium harum facere molestias. Dolor, sunt quas.',
                'user': users[i],
            }
            fake_postsss.append(dict)

        # for post in posts:
        #     num_favs = random.randint(0, 5)
        #     random.shuffle(users)
        #     for i in range(num_favs):
        #         post.favorites.create(user=users[i])

        posts = []
        for post_data in fake_postsss:
            post = Post.objects.create(**post_data)
            posts.append(post)
        print('Posts imported!!!')

        for i in range(100):
            Vote.objects.create(post=posts[random.randint(0, 50)], user=users[i])
        
        # image_list = [
        #     'blade-itself.jpg',
        #     'lies-locke-lamora.jpg',
        #     'name-wind.jpg',
        #     'ready-player-one.jpg',
        #     'storm-front.jpg',
        #     'the-martian.jpg',
        #     'three-body-problem.jpg',
        #     'way-kings.jpg',
        #     'wise-mans-fear.jpg',
        #     'wizard-earthsea',
        # ]

        with open(get_path('books.csv'), 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                post.image.save(row['cover'], File(open(get_path(row['cover']), 'rb')))
                post.save()

        print('Data imported successfully!')
