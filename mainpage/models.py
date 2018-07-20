from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    cat_name = models.CharField(max_length=50, help_text="Укажите название категории")

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Введите название товара")
    description = models.TextField(max_length=100, help_text="Введите описание товара")
    price = models.FloatField(max_length=5, help_text="Введите цену товара")
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
