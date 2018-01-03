# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
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


class CustomUser(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True  # If no new field is added.
