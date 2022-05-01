from django.db import models
from django.utils import timezone, dateformat


def get_time():
    return dateformat.format(timezone.now(), 'Y-m-d')


class FoodProducts(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.FloatField()
    date = models.DateTimeField(default=get_time)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]


class Rest(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.FloatField()
    date = models.DateTimeField(default=get_time)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]


class Stuff(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateTimeField(default=get_time)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]
