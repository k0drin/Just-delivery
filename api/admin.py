from django.contrib import admin
from .models import *

# admin.site.register(Category)

class AdminCategory(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "time_update",
        "is_published",
    )  
    search_fields = ("title",)  
    list_filter = ("time_create",)  


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
            "name",
            "price",
            "in_stock",
            "category",
        )
    search_fields = ("name",)
    list_filter = ("category",)


admin.site.register(Item, AdminItem)
