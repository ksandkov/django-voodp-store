from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import Category, Product
from .forms import ProductAddForm


def index(request):
    name = Category.cat_name
    return render(request, 'mainpage/index.html', {
        'name': name,
    })

def catalogue(request):
    return render(request, 'mainpage/catalogue.html', {
        'catalogue': Category.objects.all().order_by('cat_name'),
    })

def product(request, cat):
    catalogue_cat = Category.objects.get(id=cat)
    sorted_products = Product.objects.filter(category=cat)
    if request.method == 'GET':
        if 'sortby' in request.GET and request.GET['sortby'] == 'name_up':
            return render(request, 'mainpage/product.html', {
                'catalogue_cat': catalogue_cat,
                'sorted_products': sorted_products.order_by('name'),
            })
        elif 'sortby' in request.GET and request.GET['sortby'] == 'name_d':
            return render(request, 'mainpage/product.html', {
                'catalogue_cat': catalogue_cat,
                'sorted_products': sorted_products.order_by('-name'),
            })
        elif 'sortby' in request.GET and request.GET['sortby'] == 'price_up':
            return render(request, 'mainpage/product.html', {
                'catalogue_cat': catalogue_cat,
                'sorted_products': sorted_products.order_by('price'),
            })
        elif 'sortby' in request.GET and request.GET['sortby'] == 'price_d':
            return render(request, 'mainpage/product.html', {
                'catalogue_cat': catalogue_cat,
                'sorted_products': sorted_products.order_by('-price'),
            })
        else:
            return render(request, 'mainpage/product.html', {
                'catalogue_cat': catalogue_cat,
                'sorted_products': sorted_products,
                })

def new_product(request):
    form = ProductAddForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        category_id = form.cleaned_data['category'].id
        product_name = form.cleaned_data['name']
        messages.success(request, 'Спасибо, что добавили товар "{}".'.format(product_name))
        form.save()
        return redirect('product', category_id)
    return render(request, 'mainpage/newproduct.html', {
        'form': form,
    })
