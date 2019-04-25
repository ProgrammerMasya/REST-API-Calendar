from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(verbose_name='Event', max_length=50)
    start_datetime = models.DateTimeField(verbose_name='Start datetime')
    end_datetime = models.DateTimeField(verbose_name='End datetime', blank=True)

    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        if not self.end_datetime:
            self.end_datetime = datetime(self.start_datetime.year,
                                         self.start_datetime.month,
                                         self.start_datetime.day,
                                         23, 59, 59)
        super(Event, self).save(*args, **kwargs)