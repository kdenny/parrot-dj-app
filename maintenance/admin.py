# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from maintenance.models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Staff)
admin.site.register(MaintenanceRequest)
admin.site.register(MaintenanceUpdate)
admin.site.register(Comment)