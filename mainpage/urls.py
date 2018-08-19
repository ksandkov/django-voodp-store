from django.urls import path

from . import views
from .views import catalogue, category, new_product, product, edit_product


urlpatterns = [
    path('', catalogue, name='catalogue'),
    path('<int:cat>/', category, name='category'),
    path('addnew/', new_product, name='new_product'),
    path('<int:cat>/<int:prod>/', product, name='product'),
    path('<int:cat>/<int:prod>/edit/', edit_product, name='edit_product'),

]
