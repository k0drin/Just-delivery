from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from JustDelivery.dependency import redis_connection
from django.db.models import Model
from .serializers import CategorySerializer, UserSrializer, ItemSerializer, EmptySerializer
from django.http import JsonResponse
from django.views.generic import View
from .services.redis_storage import RedisStorage
from .services.order_container import OrderContainer


class CategoryAPIView(generics.ListAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer


class UserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSrializer


class CategoryItemsListView(generics.ListAPIView):
    serializer_class = ItemSerializer
    model = Item
    filter_field = 'name'

    def get_queryset(self):
        if self.model is None or self.serializer_class is None or self.filter_field is None:
            raise ValueError("Ensure 'model', 'serializer_class', and 'filter_field' are set.")

        filter_value = self.kwargs.get(self.filter_field)
        if filter_value is not None:
            return self.model.objects.filter(**{self.filter_field: filter_value})
        return self.model.objects.all()


class FilterListAPIView(generics.ListAPIView):
    model = None


class AddItemToCart(generics.CreateAPIView):
    serializer_class = EmptySerializer
    def post(self, request):
        item_id = request.data.get('item_id')
        user_id = request.dtat.get('user_id')

        if not item_id or not user_id:
            return Response({'message': 'not specified item_id or user_id'}, status=status.HTTP_400_BAD_REQUEST)

        cart_key = f"user:{user_id}:cart"
        redis_connection.sadd(cart_key, item_id)

        return Response({'message': 'Product successfully added to cart'}, status=status.HTTP_201_CREATED)


class AddItemToOrderView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')

        if not user_id or not product_id:
            return Response({'error': 'user_id and product_id are required'}, status=status.HTTP_400_BAD_REQUEST)

        order_container = OrderContainer(user_id, RedisStorage(conn))
        order_container.add_to_cart(product_id)

        return Response({'message': 'Product successfully added to order'}, status=status.HTTP_201_CREATED)


