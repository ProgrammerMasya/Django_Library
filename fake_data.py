import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libery.settings')

import django
django.setup()

import random
from main.models import Book, UserProfile
from faker import Faker

fake = Faker()


def create_users(num_entries=15, overwrite=False):

    if overwrite:
        UserProfile.objects.all().delete()
    for _ in range(num_entries):
        first_name = fake.first_name()
        last_name = fake.last_name()
        image = fake.image_url()
        UserProfile.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=first_name + last_name,
            password="password",
            image=image
        )


def create_books(num_entries=15, overwrite=False):

    if overwrite:
        Book.objects.all().delete()
    choices = ['Snake Of The Land', 'Army Of The North', 'Wives Without Glory', 'Priests Of The Prison',
               'Girls And Defenders', 'Slaves And Enemies', 'Wand Of Eternity', 'Spear Without Courage',
               'Meeting At The Future', 'Guarded By My Home', 'God Of The Ancestors', 'Owl Of Next Year',
               'Gods With Money', 'Butchers With Silver', 'Serpents And Witches', 'Serpents And Mice',
               'Murder Of Freedom', 'Love Of The World', 'Blood At The Dark', 'Eating At Myself']
    users = list(UserProfile.objects.all())
    for _ in range(num_entries):
        b = Book(
            name=random.choice(choices),
            author=fake.name(),
            user=random.choice(users),
            price=fake.random_int(1, 9999),
            pages_count=fake.random_int(1, 10),
            created_add=fake.date_time_this_month(),
            updated_add=fake.date_time_this_month(),
            amazon_rating=fake.random_int(1, 10)
        )
        b.save()


if __name__ == '__main__':
    create_users(20, True)
    create_books(20, True)