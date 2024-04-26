from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from dependency import *
from django.db.models import Model
from .serializers import CategorySerializer, UserSrializer, ItemSerializer, EmptySerializer


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
