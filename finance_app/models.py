from django.db import models


class FoodProducts(models.Model):
    title = models.CharField(max_length=100, unique=True)
    amount = models.IntegerField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]
