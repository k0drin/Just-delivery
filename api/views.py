from rest_framework import generics
from django.shortcuts import render
from .models import *
from .serializers import CategorySerializer

def all_category(request):
    category = Category.objects.all()
    return render(request, 'api/index.html', {'category': category})

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
