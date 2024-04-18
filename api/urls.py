# это рабочий код
from django.contrib import admin
from django.urls import path
from api.views import CategoryAPIView, UserAPIView


urlpatterns = [
    path('category/', CategoryAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
 
]
