from django.db import models
from django.contrib.auth.models import AbstractUser


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)


class Hero(models.Model):
    hero_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

