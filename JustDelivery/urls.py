from django.contrib import admin
from django.urls import path
from api.views import all_category

urlpatterns = [
    path('', all_category),
    path('admin/', admin.site.urls),
    #path('all_category/', all_category, name='All category')
]
