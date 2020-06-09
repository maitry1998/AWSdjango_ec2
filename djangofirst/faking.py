# import os
# import composeexample
# os.environ.setdefault("DJANGO_SETTINGS_MODULE","composeexample.settings")
#
# import django
# django.setup()

import random
from djangofirst.models import Topic,Webpage,AccessRecord
from faker import Faker


fake=Faker()
topics=["A","b","c","d"]


def add_topic():
    t = Topic.objects.get_or_create(top_name="tyyyyoppp")[0]
    t.save()
    return t

def populate(N=5):
    web_name=fake.company()
    web_url=fake.url()
    webpage=Webpage.objects.get_or_create(topic=add_topic(),name=web_name,url=web_url)[0]
    webpage.save()
    accessrecord = AccessRecord.objects.get_or_create(Webpage=webpage, date=fake.date())[0]
    accessrecord.save()

populate()