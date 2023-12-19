import uuid
from django.db import models
from django.utils import timezone, dateformat
from datetime import datetime


def get_time():
    return dateformat.format(timezone.now(), "Y-m-d")


# class User(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=100, null=False)
#     time_create = models.DateField(default = get_time)
#     time_update = models.DateField(default = get_time)


# class UserSettings(models.Model):  ## write smth about user restrictions for their spents
#     ...

## class Currency(models.Model) ## persistent currancy data (rubles, dollars, etc)

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=True)
    # user = models.UUIDField(null=True)
    archive = models.BooleanField(default=False)
    time_create = models.DateField(default=get_time)
    time_update = models.DateField(default=get_time)

    def __str__(self):
        return self.name


class Spent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=500, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # user = models.UUIDField(null=True)
    archive = models.BooleanField(default=False)
    time_create = models.DateField(default=get_time)
    time_update = models.DateField(default=get_time)

    def __str__(self):
        return f"{self.name}: {self.price}"


def get_month():
    today = datetime.today()
    datem = datetime(today.year, today.month, 1)
    output = ""
    if "-01-" in str(datem):
        output = "January"
    elif "-02-" in str(datem):
        output = "February"
    elif "-03-" in str(datem):
        output = "March"
    elif "-04-" in str(datem):
        output = "April"
    elif "-05-" in str(datem):
        output = "May"
    elif "-06-" in str(datem):
        output = "June"
    elif "-07-" in str(datem):
        output = "July"
    elif "-08-" in str(datem):
        output = "August"
    elif "-09-" in str(datem):
        output = "September"
    elif "-10-" in str(datem):
        output = "October"
    elif "-11-" in str(datem):
        output = "November"
    else:
        output = "December"
    return str(output)


class SStuff(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateTimeField(default=get_time)
    month = models.TextField(default=get_month)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]


class FFoodProducts(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(default=get_time)
    month = models.TextField(default=get_month)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]


class Stuffs(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateTimeField(default=get_time)
    month = models.TextField(default=get_month)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]


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
