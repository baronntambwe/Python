import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## FAKE POPULATION SCRIPT

import random
from first_app.models import Topic, AccessRecord, WebPage
from faker import Faker

fakegen = Faker()
topics = ['Social', 'Search', 'Marketplace', 'Games', 'News']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]    # If it does not exist, it creates
    t.save()

    return t

