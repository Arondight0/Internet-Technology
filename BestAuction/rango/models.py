from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    # This line is requiored. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    bidlist = models.ManyToManyField('Page', related_name='b+', blank=True)
    ownlist = models.ManyToManyField('Page', related_name='o+', blank=True)

    # The additional attributes we wish to include.
    name = models.CharField(max_length=128)
    email = models.URLField(blank=True)
    phone = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    description = models.CharField(max_length=1000)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    startprice = models.FloatField(default=0)
    highestprice = models.FloatField(default=0)
    bestbidder = models.CharField(max_length=128)
    closingtime = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(UserProfile)
    status = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)


    def __str__(self):  # For Python 2, use __unicode__ too
        return self.title

