from django.contrib import admin
from django.urls import path
from api.views import all_category 
from api.views import CategoryAPIView

urlpatterns = [
    path('', all_category),
    path('admin/', admin.site.urls),
    #path('all_category/', all_category, name='All category')
    path('api/v1/listcategory/', CategoryAPIView.as_view())
]
