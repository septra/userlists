from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    dob = models.DateField(null=False)

    def __unicode__(self):
        return """
                Username: {userName}
                First Name: {firstName}
                Last Name: {lastName}
                """.format(
                    userName = self.user.username,
                    firstName = self.user.first_name,
                    lastName = self.user.last_name
                )

class Item(models.Model):
    userprofile = models.ForeignKey(UserProfile)
    text = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s : %s" % (self.user.userName, self.text)
