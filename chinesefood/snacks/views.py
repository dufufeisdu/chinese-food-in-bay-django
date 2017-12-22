# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("All my favorate snacks")
# Create your views here.
