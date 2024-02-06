import uuid
from django.db import models
from django.utils import timezone, dateformat


def get_time():
    return dateformat.format(timezone.now(), "Y-m-d")


class Category(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=True)
    archive = models.BooleanField(default=False)
    time_create = models.DateField(default=get_time)
    time_update = models.DateField(default=get_time)

    def __str__(self):
        return self.name


class Spent(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=500, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)
    time_create = models.DateField(default=get_time)
    time_update = models.DateField(default=get_time)

    def __str__(self):
        return f"{self.name}: {self.price}"

