from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    def __repr__(self):
        return self.name

class Item(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=100)

    def __str__(self):
        return "%s : %s" % (self.user.name, self.text)
    def __unicode__(self):
        return "%s : %s" % (self.user.name, self.text)
    def __repr__(self):
        return "%s : %s" % (self.user.name, self.text)
