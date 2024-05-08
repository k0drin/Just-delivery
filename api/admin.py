from django.contrib import admin
from .models import *

# admin.site.register(Category)


# Презентація моделі в інтерфейсі адміністратора
class AdminCategory(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "time_update",
        "is_published",
    )  # Какие поля отображать в списке объектов
    search_fields = ("title",)  # Поля для поиска
    list_filter = ("time_create",)  # Фильтры по дате создания


admin.site.register(Category, AdminCategory)


# admin.site.register(User)
class AdminUser(admin.ModelAdmin):
    model = User
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "address",
        "time_create",
    )
    search_fields = ("last_name", "phone_number", "address")
    list_filter = ["time_update"]

admin.site.register(User, AdminUser)

class AdminItem(admin.ModelAdmin):
    model = Item
    list_display = (
            "id",   
            "name",
            "price",
            "in_stock",
            "category",
        )
    search_fields = ("name",)
    list_filter = ("category",)


admin.site.register(Item, AdminItem)
