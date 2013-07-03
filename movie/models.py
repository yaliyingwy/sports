import hashlib
import random
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)
    score = models.FloatField()
    content = models.TextField()
    image = models.ImageField(upload_to='static/img')
    ftp = models.URLField(default="ftp://192.168.5.88")
    validate = models.BooleanField()
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-update_time']


class User(models.Model):
    name = models.CharField(max_length=10,primary_key=True)
    email = models.EmailField(unique=True)
    passwd = models.CharField(max_length=100)

    def set_passwd(self):
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        hsh = hashlib.sha1(salt + self.passwd).hexdigest()
        self.passwd = '%s#%s' % (salt, hsh)

    def check_passwd(self, raw_passwd):
        salt, hsh = self.passwd.split('#')
        return hsh == hashlib.sha1(salt + raw_passwd).hexdigest()

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    content = models.TextField()
    update_time = models.DateTimeField(auto_now=True)
    pid = models.IntegerField(default=0)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ['update_time']


@receiver(pre_save, sender=User)
def my_handler(sender, instance, *args, **kwargs):
    instance.set_passwd()
