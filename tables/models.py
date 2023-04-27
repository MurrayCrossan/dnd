from django.db import models

# Create your models here.

class Table(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class TableEntry(models.Model):
    table = models.ForeignKey(Table, blank=True, null=True, on_delete=models.CASCADE)
    snip = models.CharField(max_length=200)
    entry = models.TextField()
    cr = models.CharField(max_length=20)
    
    def getName(table):
        return str(table) + ' Entry'
    
    name = getName(table)

    def __str__(self):
        return self.name

    