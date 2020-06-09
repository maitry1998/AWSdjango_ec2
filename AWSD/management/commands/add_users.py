from django.core.management.base import BaseCommand
from faker import Faker
from AWSD.models import MembersModel,ActivityModel
from datetime import datetime
import random
import pytz
import string
from rest_framework.reverse import reverse
from django.utils import timezone
import urllib, json
import urllib.request


class Command(BaseCommand):
    help = 'Stores and displays dummy values sent by users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()
        TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
        for i in range(total):
            a=ActivityModel.objects.create(start_time=datetime.now(tz=timezone.utc),end_time=datetime.now(tz=timezone.utc))
            a1 = ActivityModel.objects.create(start_time=datetime.now(tz=timezone.utc),
                                             end_time=datetime.now(tz=timezone.utc))
            m=MembersModel.objects.create(ppid=''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=6))
                                   , real_name=fake.name()
                                   , tz=random.choice(TIMEZONES))
            m.Members_periods.add(a)
            m.Members_periods.add(a1)

            url="http://127.0.0.1:8000"+reverse('members-detail', args=[m.ppid])
            response = urllib.request.urlopen(url).read()
            # import pdb;pdb.set_trace()
            data = json.loads(response)
            self.stdout.write(str(data))
