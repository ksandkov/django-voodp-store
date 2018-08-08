from django.urls import path, include
from django.conf.urls import url

from . import views
from .views import index, catalogue, category, new_product, register, product, edit_product


urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('catalogue/<int:cat>/', category, name='category'),
    path('catalogue/addnew/', new_product, name='new_product'),
    path('accounts/register/', register, name='register'),
    path('catalogue/<int:cat>/<int:prod>/', product, name='product'),
    path('catalogue/<int:cat>/<int:prod>/edit/', edit_product,
         name='edit_product'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
