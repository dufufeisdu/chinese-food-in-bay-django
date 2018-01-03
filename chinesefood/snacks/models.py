# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator

# Create your models here.
# snacks: name origin flavor cookingstep whereTobuy


class Snack(models.Model):
    snack_name = models.CharField(max_length=200)
    snack_origin = models.CharField(max_length=200)
    snack_flavor = models.CharField(max_length=200)
    snack_cooking_step = models.CharField(max_length=200)
    snack_image_url = models.CharField(max_length=200)
    snack_liked = models.IntegerField(default=0)


class UserLikesSnack(models.Model):
    snack_name = models.CharField(max_length=200)
    liks_number = models.IntegerField(default=0)


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
