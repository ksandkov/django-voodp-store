from django.contrib import admin

from .models import Category, Product


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category', 'user', 'is_approved', 'slug']
    list_filter = ('name', 'is_approved',)
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_name', 'slug']
    prepopulated_fields = {'slug': ('cat_name',)}


admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
