from django.db import models
import pytz
# Create your models here.

class ActivityModel(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.start_time)

class MembersModel(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    ppid = models.CharField(max_length=6,unique=True, primary_key=True)
    real_name = models.CharField(max_length=350, unique=True)
    tz = models.CharField(max_length=32, choices=TIMEZONES,
                          default='UTC')
    Members_periods = models.ManyToManyField(ActivityModel)

    def __str__(self):
        return self.real_name

