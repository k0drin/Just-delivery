from rest_framework import generics
from .models import *
from .serializers import CategorySerializer, UserSrializer, ItemSerializer

class CategoryAPIView(generics.ListAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer

class UserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSrializer

class CategoryItemsListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer





