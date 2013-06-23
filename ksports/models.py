#encoding=utf-8
from django.db import models
from django.utils import timezone
import datetime


class Sports(models.Model):
    '''we have sports every week'''
    sports_choices = (
            (u'pingpong', u'乒乓球'),
            (u'yumao', u'羽毛球'),
            (u'youyong', u'游泳'),
            )
    name = models.CharField(max_length=10, choices=sports_choices, primary_key=True)
    
    def __unicode__(self):
        return self.get_name_display()


class Person(models.Model):
    '''a person can only take in one sport'''
    name = models.CharField(max_length=10, blank=False, primary_key=True)
    sports = models.ForeignKey(Sports)
    update_time = models.DateTimeField(auto_now=True)

    def inAWeek(self):
        delta = datetime.datetime.now() - self.update_time.astimezone(timezone.utc).replace(tzinfo=None)
        return delta.days < 5

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-update_time']


class Message(models.Model):
    '''message for everyone'''
    content = models.TextField(blank=False)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content

    class Meta:
        ordering = ['-update_time']
