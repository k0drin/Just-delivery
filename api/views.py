from rest_framework import generics
from .models import *
from .serializers import CategorySerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        print("CategoryAPIView called")
        return super().get(request, *args, **kwargs)
