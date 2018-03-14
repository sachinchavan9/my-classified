# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import State, City, Category, SubCategory, PostAdd


def home(request):
    states = State.objects.all()
    return render(request, 'advert/home.html', {'states': states})


def district_view(request, slug):
    slug = str(slug).replace("-", " ")
    cities = get_object_or_404(City, city_name=slug)
    cat = Category.objects.filter(city=cities.pk)
    return render(request, 'advert/city_view.html', {'cat': cat, 'cities': cities})


def add_view(request, slug, pk):
    sub_cat_add = get_object_or_404(SubCategory, pk=pk)
    return render(request, 'advert/add_post.html', {'sub_cat_add': sub_cat_add})


def advert(request, title, pk):
    addvert = get_object_or_404(PostAdd, pk=pk)
    return render(request, 'advert/advert.html', {'addvert': addvert})
