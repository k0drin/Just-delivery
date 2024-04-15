# это рабочий код
from django.contrib import admin
from django.urls import path
from api.views import CategoryAPIView


urlpatterns = [
    path('v1/category/', CategoryAPIView.as_view())
]