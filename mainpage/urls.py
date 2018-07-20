from django.urls import path
from .views import index, catalogue, product

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('catalogue/<int:catalogue_id>/', product),
]
