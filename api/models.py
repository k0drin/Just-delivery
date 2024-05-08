from django.db import models
import hashlib
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    # For loggin
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    # Для відображення назв
    def __str__(self):
        return self.title

    # Для того щоб була кнопка "дивитись на сайті"
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})


class HashField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 64  # SHA-256 hash size in hex is 64 characters
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)
        return self.get_hashed_value(value)

    def get_hashed_value(self, value):
        """Returns the SHA-256 hash of the value."""
        if value is None:
            return None
        return hashlib.sha256(str(value).encode()).hexdigest()

    def from_db_value(self, value, expression, connection):
        """Converts the value from the database to the format expected by the application."""
        return value

    def to_python(self, value):
        """Converts the value from the database or from the serializer into the correct Python object."""
        return value


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=255, unique=True, null=False)
    address = models.CharField(max_length=255, unique=True, null=False)
    tid = HashField(null=True)
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.address


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="", default="")
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    user_id = models.CharField(max_length=100)
    items = models.JSONField()