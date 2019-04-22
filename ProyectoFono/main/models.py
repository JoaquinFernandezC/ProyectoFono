from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    period = models.IntegerField()
    registered_users = models.IntegerField()
    price = models.IntegerField()
    payment_method = models.CharField(max_length=500)
