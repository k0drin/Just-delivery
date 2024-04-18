from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    # Для логирования
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    # Для отображения названий
    def __str__(self):
        return self.title

    # Чтобы была кнопка "смотреть на сайте"
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=255, unique=True, null=False)
    address = models.CharField(max_length=255, unique=True, null=False)
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.address
