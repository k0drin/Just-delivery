from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from JustDelivery.dependency import get_redis
from django.db.models import Model
from .serializers import (
    CategorySerializer,
    UserSrializer,
    ItemSerializer,
    EmptySerializer,
)
from django.http import JsonResponse
from django.views.generic import View
from .services.redis_storage import RedisStorage
from .services.order_container import OrderContainer
from .generics import FilterListAPIView

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSrializer


class CategoryItemsListView(FilterListAPIView):
    serializer_class = ItemSerializer
    model = Item
    filter_field = "name"



class AddItemToOrderView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        product_id = request.data.get("product_id")

        if not user_id or not product_id:
            return Response(
                {"error": "user_id and product_id are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order_container = OrderContainer(user_id, RedisStorage(get_redis()))
        order_container.add_to_cart(product_id, 1)

        return Response(
            {"message": "Product successfully added to order"},
            status=status.HTTP_201_CREATED,
        )


class RemoveItemFromOrderView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        product_id = request.data.get("product_id")

        if not user_id or not product_id:
            return Response(
                {"error": "user_id and product_id are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order_container = OrderContainer(user_id, RedisStorage(conn))
        order_container.remove_from_cart(product_id)

        return Response(
            {"message": "Product successfully removed from order"},
            status=status.HTTP_200_OK,
        )


class OrderPreviewView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response(
                {"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        order_container = OrderContainer(user_id, RedisStorage(conn))
        order_items = order_container.get_order_items()
        total_sum = sum(order_items.values())

        return Response(
            {"order_items": order_items, "total_sum": total_sum},
            status=status.HTTP_200_OK,
        )


class OrderCheckoutView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")

        if not user_id:
            return Response(
                {"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        order_container = OrderContainer(user_id, RedisStorage(conn))
        order_items = order_container.get_order_items()
        order = Order.objects.create(user_id=user_id, items=order_items)

        return Response(
            {"message": "Order finalized successfully", "order_id": order.id},
            status=status.HTTP_201_CREATED,
        )


class UserOrdersListView(APIView):
    def get(self, request):
        user_id = request.query_params.get("user_id")

        if not user_id and user_id is None:
            return Response(
                {"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        orders = Order.objects.filter(user_id=user_id)

        serialized_orders = [{"id": order.id, "items": order.items} for order in orders]
        return Response(serialized_orders, status=status.HTTP_200_OK)
