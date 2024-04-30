from django.contrib import admin
from django.urls import path
from api.views import CategoryAPIView, UserAPIView, CategoryItemsListView, AddItemToOrderView, RemoveItemFromOrderView, OrderPreviewView


urlpatterns = [
    path('category/', CategoryAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('items/<int:category_id>/', CategoryItemsListView.as_view(), name='category-items-list'),
    path('order/add_item/', AddItemToOrderView.as_view(), name='add_item_to_order'),
    path('order/remove_item/', RemoveItemFromOrderView.as_view(), name='remove_item_from_order'),
    path('order/preview/', OrderPreviewView.as_view(), name='get_all_items_and_sum'),

]
