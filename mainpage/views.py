from django.http import HttpResponse
from django.shortcuts import render

from .models import Category, Product

def index(request):
    name = Category.cat_name
    return render(request, 'mainpage/index.html', {
        'name': name,
    })

def catalogue(request):
    return render(request, 'mainpage/catalogue.html', {
        'catalogue': Category.objects.all().order_by('cat_name'),
    })

def product(request, catalogue_id):
    return render(request, 'mainpage/product.html', {
        'catalogue_id': Category.objects.get(id=catalogue_id),
        'sorted_products': Product.objects.filter(category=catalogue_id).order_by('name'),
    })
