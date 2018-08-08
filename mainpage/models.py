from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    cat_name = models.CharField(max_length=50,
                                help_text="Укажите название категории")
    slug = models.SlugField(max_length=100, null=True)

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Введите название товара")
    slug = models.SlugField(max_length=100, null=True)
    description = models.TextField(max_length=100,
                                   help_text="Введите описание товара")
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                help_text="Введите цену товара")
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        null=True, blank=True,
        on_delete=models.SET_NULL)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
