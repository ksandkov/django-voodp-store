from django.contrib import admin

from .models import Category, Product

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category']
    list_filter = ('name', )
    search_fields = ['name', 'description']
    # class Meta:
    #     model = Product

admin.site.register(Category)
admin.site.register(Product, AdminProduct)
