# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class State(models.Model):
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return self.state_name

    def get_cities(self):
        return self.State_p.all()


class City(models.Model):
    city_name = models.CharField(max_length=100)
    state = models.ForeignKey(State, related_name='State_p')

    def __str__(self):
        return self.city_name

    def get_categories(self):
        return self.City_p.all()


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='City_p')

    def __str__(self):
        return self.category_name

    def get_sub_categories(self):
        return self.Category_p.all()


class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='Category_p')

    def __str__(self):
        return self.sub_category_name

    def get_post_add(self):
        return self.SubCategory_p.all().order_by('-posted_date')


class PostAdd(models.Model):
    add_title = models.CharField(max_length=200)
    image = models.FileField(upload_to='image/', null=True, blank=True)
    add_body = models.TextField(max_length=2000)
    posted_by = models.ForeignKey('auth.User', related_name='add_owner')
    posted_date = models.DateTimeField(auto_now_add=True)
    subcategory = models.ForeignKey(SubCategory, related_name='SubCategory_p')

    def __str__(self):
        return self.add_title
