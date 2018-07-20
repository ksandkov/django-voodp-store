from django.urls import path
from .views import catalogue, product

urlpatterns = [
    path('', catalogue, name='catalogue'),
    path('<int:catalogue_id>/', product),
]
