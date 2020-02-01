import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## FAKE POPULATION SCRIPT

import random
from first_app.models import Topic, AccessRecord, WebPage, User
from faker import Faker

fakegen = Faker()
topics = ['Social', 'Search', 'Marketplace', 'Games', 'News']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]    # If it does not exist, it creates
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

            # get the Topic for the entry
            top = add_topic()

            # create the fake data for that entry
            fake_url = fakegen.url()
            fake_date = fakegen.date()
            fake_name = fakegen.company()

            # create a new webpage entry
            webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

            # create a fake access record for that webpage
            acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

            # create the fake data for the user
            fake_firstName = fakegen.first_name()
            fake_lastName = fakegen.last_name()
            fake_email = fakegen.email()

            # create fake user
            user = User.objects.get_or_create(firstName=fake_firstName, lastName=fake_lastName, email=fake_email)


if __name__ == '__main__':
    print('Populating fake data')
    populate(20)
    print('Population complete!')


    



