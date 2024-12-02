from django.urls import re_path
from api.views import (
    CategoryAPIView,
    UserAPIView,
    CategoryItemsListView,
    AddItemToOrderView,
    RemoveItemFromOrderView,
    OrderPreviewView,
    OrderCheckoutView,
    UserOrdersListView,
)


urlpatterns = [
    re_path("category/", CategoryAPIView.as_view()),
    re_path("user/", UserAPIView.as_view()),
    re_path("items/<int:category_id>/", CategoryItemsListView.as_view(), name="category-items-list"),
    re_path("order/add_item/", AddItemToOrderView.as_view(), name="add_item_to_order"),
    re_path("order/remove_item/", RemoveItemFromOrderView.as_view(), name="remove_item_from_order"),
    re_path("order/preview/", OrderPreviewView.as_view(), name="get_all_items_and_sum"),
    re_path("order/checkout/", OrderCheckoutView.as_view(), name="create_order_record"),
    re_path("orders/", UserOrdersListView.as_view(), name="all_orders_from_user"),
]
