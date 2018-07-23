from django.urls import path

from .views import index, catalogue, product, new_product


urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('catalogue/<int:cat>/', product, name='product'),
    path('catalogue/addnew/', new_product, name='new_product'),
]
