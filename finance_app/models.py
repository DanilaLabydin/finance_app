from django.db import models
from django.utils import timezone, dateformat


def get_time():
    return dateformat.format(timezone.now(), 'Y-m-d')


def get_month():
    return dateformat.format(timezone.now(), 'm')


class FoodProducts(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(default=get_time)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]


class Rest(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(default=get_time)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]


class Stuff(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateTimeField(default=get_time)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]


class Stuffs(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateTimeField(default=get_time)
    month = models.DateTimeField(default=get_month)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]