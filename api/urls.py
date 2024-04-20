from django.contrib import admin
from django.urls import path
from api.views import CategoryAPIView, UserAPIView, CategoryItemsListView


urlpatterns = [
    path('category/', CategoryAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('item/<int:category_id>/', CategoryItemsListView.as_view(), name='category-items-list'),

]
