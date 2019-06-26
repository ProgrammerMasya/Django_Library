import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libery.settings')

import django
django.setup()

import random
from libery.main.models import Book, UserProfile
from faker import Faker

fakegen = Faker()

fakegen.name()
