from django.shortcuts import render
from .models import *


def all_category(request):
    category = Category.objects.all()
    return render(request, 'api/index.html', {'category': category})
