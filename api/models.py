from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    # направление кухни: грузинская, украинская, армянская...
    direction = models.CharField(max_length=255)
    description = models.TextField
    # для логирования
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

class Order(models.Model):
    user_name = models.CharField(max_length=255)
    user_id = models.IntegerField
    user_email = models.EmailField
    text = models.TextField
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
