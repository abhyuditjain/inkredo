# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Company model
# Currently has name and datetime fields
class Company(models.Model):
    company_name = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.company_name

# User model referencing the company
# ON DELETE CASCADE so it's deleted if company is deleted
class User(models.Model):
    user_name = models.CharField(max_length = 200)
    first_name = models.CharField(max_length = 200, null = True, blank = True)
    last_name = models.CharField(max_length = 200, null = True, blank = True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)