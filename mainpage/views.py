from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify

from .models import Category, Product
from .forms import ProductAddForm, RegistrationForm
from unidecode import unidecode

def index(request):
    name = Category.cat_name
    random_products = Product.objects.filter(is_approved=True)
    return render(request, 'mainpage/index.html', {
        'random_products': random_products,
    })


def catalogue(request):
    catalogue = Category.objects.all().order_by('cat_name')
    if 'search' in request.GET:
        catalogue = catalogue.filter(cat_name__contains=request.GET['search'])
    return render(request, 'mainpage/catalogue.html', {
        'catalogue': catalogue,
    })


def category(request, cat):
    catalogue_cat = get_object_or_404(Category, pk=cat)
    sorted_products = Product.objects.filter(category=cat).filter(is_approved=True)
    paginator = Paginator(sorted_products, 3)
    page = request.GET.get('page')
    page_paginate = paginator.get_page(page)
    products = Product.objects.filter(category=cat).filter(is_approved=True)


    if request.method == 'GET':
        if 'search' in request.GET:
            sorted_products = sorted_products.filter(name__contains=request.GET['search'])
            amount = sorted_products.count()

            return render(request, 'mainpage/category.html', {
                'catalogue_cat': catalogue_cat,
                'sorted_products': sorted_products,
                'catalogue': Category.objects.all().order_by('cat_name'),
                'products': products,
                'amount': amount,
            })
        if 'sortby' in request.GET and request.GET['sortby'] == 'name_up':
            return render(request, 'mainpage/category.html', {
                'catalogue_cat': catalogue_cat,
                'sorted_products': sorted_products.order_by('name'),
                'catalogue': Category.objects.all().order_by('cat_name'),
                'products': products,
            })
        elif 'sortby' in request.GET and request.GET['sortby'] == 'name_d':
            return render(request, 'mainpage/category.html', {
                'catalogue_cat': catalogue_cat,
                'sorted_products': sorted_products.order_by('-name'),
                'catalogue': Category.objects.all().order_by('cat_name'),
                'products': products,
            })
        elif 'sortby' in request.GET and request.GET['sortby'] == 'price_up':
            return render(request, 'mainpage/category.html', {
                'catalogue_cat': catalogue_cat,
                'sorted_products': sorted_products.order_by('price'),
                'catalogue': Category.objects.all().order_by('cat_name'),
                'products': products,
            })
        elif 'sortby' in request.GET and request.GET['sortby'] == 'price_d':
            return render(request, 'mainpage/category.html', {
                'catalogue_cat': catalogue_cat,
                'sorted_products': sorted_products.order_by('-price'),
                'catalogue': Category.objects.all().order_by('cat_name'),
                'products': products,
            })
        else:
            return render(request, 'mainpage/category.html', {
                'catalogue_cat': catalogue_cat,
                'sorted_products': paginator.page(request.GET.get('page', 1)),
                'catalogue': Category.objects.all().order_by('cat_name'),
                'paginator': paginator,
                'page_paginate': page_paginate,
                'products': products,
            })


def product(request, cat, prod):
    item = get_object_or_404(Product, pk=prod)
    return render(request, 'mainpage/product.html', {
        'item': item,
    })


def edit_product(request, cat, prod):
    try:
        instance = Product.objects.get(pk=prod)
    except Product.DoesNotExist:
        raise PermissionDenied
    if request.user != instance.user:
        raise PermissionDenied
    if request.method == 'POST':
        form = ProductAddForm(request.POST, instance=instance)
        messages.success(request, 'Товар  успешно изменён.')
        form.save()
        return HttpResponseRedirect(reverse('product', kwargs={'cat': cat, 'prod': prod}))
    else:
        form = ProductAddForm(instance=instance)
    return render(request, 'mainpage/editproduct.html', {
        'form': form,
        'instance': instance,
    })


def new_product(request):
    if request.user.is_authenticated:
        form = ProductAddForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            category_id = form.cleaned_data['category'].id
            product_name = form.cleaned_data['name']
            inst = form.save()
            inst.user = request.user
            inst.slug = slugify(unidecode(product_name))
            inst.save()
            messages.success(request, 'Спасибо, ваш товар "{}" будет успешно добавлен.'.format(
                            product_name)
                            )
            return HttpResponseRedirect(reverse('category', kwargs={'cat': category_id}))
        return render(request, 'mainpage/newproduct.html', {
            'form': form,
        })
    else:
        raise PermissionDenied


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'mainpage/register.html', {
        'form': form,
    })
