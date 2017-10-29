# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from packagemanager.models import Resident, Apartment
from django.contrib.auth.models import User

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    account = models.OneToOneField(User)

    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return unicode(self.name)

class Category(models.Model):
    name = models.CharField(max_length=150)
    staff = models.ManyToManyField(Staff)

    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return unicode(self.name)

class MaintenanceRequest(models.Model):
    resident = models.ForeignKey(Resident)
    apartment_no = models.ForeignKey(Apartment)
    date_submitted = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    status = models.CharField(max_length=100, default='pending')
    description = models.TextField()
    staff = models.ManyToManyField(Staff)

    def __unicode__(self):
        return unicode(self.resident.name + "-" + self.category.name + "-" + str(self.date_submitted))

    def __str__(self):
        return unicode(self.resident.name + "-" + self.category.name + "-" + str(self.date_submitted))

class MaintenanceUpdate(models.Model):
    comment = models.TextField()
    request = models.ForeignKey(MaintenanceRequest, related_name='updates')
    staff = models.ForeignKey(Staff)
    date = models.DateTimeField(auto_now_add=True)
    update_type = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(str(self.request.id) + "-" + self.update_type + "-" + str(self.date))

    def __str__(self):
        return unicode(str(self.request.id) + "-" + self.update_type + "-" + str(self.date))

class Comment(models.Model):
    submitted_by = models.ForeignKey(Resident)
    request = models.ForeignKey(MaintenanceRequest)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()