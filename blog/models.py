from codecs import getencoder
from operator import mod
from pyexpat import model
from subprocess import CREATE_NO_WINDOW
from tkinter import CASCADE
from typing import Type
from unicodedata import name
from unittest import case
from django.db import models
from django.contrib.auth.models import User

GENDER = (
    (0, "Male"),
    (1, "Female"),
    (2, "Other")
)

RACES = (
    (0, "Human"),
    (1, "Dwarf"),
    (2, "Elf")
)

class Continent(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tag = models.CharField(max_length=280, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name
    
    def __name__(self):
        return "Continent"

class Nation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    continent = models.ForeignKey(Continent, blank=True, null=True, on_delete=models.CASCADE)
    tag = models.CharField(max_length=280, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=False)

    def __str__(self):
        return self.name

    def __name__():
        return "Nation"

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nation = models.ForeignKey(Nation, null=True, on_delete=models.CASCADE)
    tag = models.CharField(max_length=280, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def __name__(self):
        return "Location"

class Organisation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    fname = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    gender = models.IntegerField(choices=GENDER, default=0)
    race = models.IntegerField(choices=RACES, default=0)
    occupation = models.CharField(max_length=100)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    orgMember = models.ManyToManyField(Organisation, blank=True)
    tag = models.CharField(max_length=280, null=True, blank=True)
    context = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.fname + " " +self.sname

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fname', 'sname'], name='unique_name')
        ]

class Shop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=100)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Ship(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    captain = models.ForeignKey(Person, null=True, on_delete=models.CASCADE, related_name="ship_captain")
    crew = models.ManyToManyField(Person, blank=True)
    port = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    effect = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name