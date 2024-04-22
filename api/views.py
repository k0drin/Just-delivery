from rest_framework import generics
from .models import *
from django.db.models import Model
from .serializers import CategorySerializer, UserSrializer, ItemSerializer

class CategoryAPIView(generics.ListAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer

class UserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSrializer

#class CategoryItemsListView(generics.ListAPIView):
#    queryset = Item.objects.all()
#    serializer_class = ItemSerializer

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

                        
