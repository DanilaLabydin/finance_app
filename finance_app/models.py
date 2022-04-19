from django.db import models
from django.utils import timezone


def get_time():
    return timezone.now()


class FoodProducts(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.FloatField()
    date = models.DateTimeField(default=get_time)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]
