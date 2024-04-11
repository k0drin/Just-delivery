from django.db import models

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

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
