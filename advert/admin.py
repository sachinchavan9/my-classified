# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import SubCategory, PostAdd, MyProfile

admin.site.register(SubCategory)
admin.site.register(PostAdd)
admin.site.register(MyProfile)
